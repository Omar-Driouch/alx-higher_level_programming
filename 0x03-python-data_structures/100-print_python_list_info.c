#include <Python.h>

/**
 * print_python_list_info - Prints basic data about Python lists.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	int size, alc, idx;
	PyObject *obj;

	size = Py_SIZE(p);
	alc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alc);

	for (idx = 0; idx < size; idx++)
	{
		printf("Element %d: ", idx);

		obj = PyList_GetItem(p, idx);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}