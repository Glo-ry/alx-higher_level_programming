/*
 * File: 103-python.c
 * Auth: Type Your Name Here
 */

#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Prints basic info about Python lists.
 * @p: A PyObject list object
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, index;
	PyObject *item;

	if (!PyList_Check(p))
	{
		printf("[*] Python list info\n");
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	size = PyObject_Length(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);

	for (index = 0; index < size; index++)
	{
		item = PyList_GetItem(p, index);
		printf("Element %ld: %s\n", index, Py_TYPE(item)->tp_name);
		if (PyBytes_Check(item))
			print_python_bytes(item);
		else if (PyFloat_Check(item))
			print_python_float(item);
	}
}

/**
 * print_python_bytes - Prints basic info about Python bytes.
 * @p: A PyObject bytes object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, index;
	char *data;

	if (!PyBytes_Check(p))
	{
		printf("[.] bytes object info\n");
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	data = PyBytes_AsString(p);

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", data);

	size = size < 10 ? size + 1 : 10;
	printf("  first %ld bytes:", size);

	for (index = 0; index < size; index++)
		printf(" %02hhx", data[index]);

	printf("\n");
}

/**
 * print_python_float - Prints basic info about Python float objects.
 * @p: A PyObject float object
 */
void print_python_float(PyObject *p)
{
	if (!PyFloat_Check(p))
	{
		printf("[.] float object info\n");
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	printf("[.] float object info\n");
	printf("  value: %f\n", PyFloat_AS_DOUBLE(p));
}
