#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: pointer to PyObject
 *
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t list_size, list_allocated, i;
	PyObject *item;

	list_size = PyList_Size(p);
	list_allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %zd\n", list_size);
	printf("[*] Allocated = %zd\n", list_allocated);

	for (i = 0; i < list_size; i++)
	{
		printf("Element %zd: ", i);

		item = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(item)->tp_name);
	}
}
