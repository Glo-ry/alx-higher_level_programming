#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - This function prints bytes information
 *
 * @p: Python Object
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *byte_obj = (PyBytesObject *)p;
	PyVarObject *var_obj = (PyVarObject *)p;
	char *string = byte_obj->ob_sval;
	long int size = var_obj->ob_size;
	long int limit, i;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string);

	if (size >= 10)
		limit = 10;
	else
		limit = size + 1;

	printf("  first %ld bytes:", limit);

	for (i = 0; i < limit; i++)
	{
		unsigned char byte = (unsigned char)string[i];
		printf(" %02x", byte);
	}

	printf("\n");
}

/**
 * print_python_list - Thus function prints list information
 *
 * @p: Python Object
 * Return: void
 */
void print_python_list(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	long int size = Py_SIZE(list);
	long int allocated = list->allocated;
	long int i;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (i = 0; i < size; i++)
	{
		PyObject *obj = list->ob_item[i];
		printf("Element %ld: %s\n", i, Py_TYPE(obj)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}
