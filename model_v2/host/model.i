//
// ELL SWIG interface for module model
//

%module(directors="1", moduleimport="import $module") model
%feature("autodoc", "3");

%include "stdint.i"

%include "vector.i"

// Propagate python callback exceptions
%feature("director:except") {
    if ($error != NULL) {
        PyObject* ptype = nullptr;
        PyObject* pvalue = nullptr;
        PyObject* ptraceback = nullptr;
        PyErr_Fetch(&ptype, &pvalue, &ptraceback);
        PyErr_Restore(ptype, pvalue, ptraceback);
        PyErr_Print();
        Py_Exit(1);
    }
}

%{
#include "model.i.h"
%}

%feature("director") ModelWrapper;


#if defined(SWIGPYTHON)
%pythoncode %{


_model_wrapper = None

def predict(inputData: 'numpy.ndarray') -> "numpy.ndarray":
    """Convenience function for calling the model directly without callbacks"""
    global _model_wrapper
    if _model_wrapper is None:
        _model_wrapper = ModelWrapper()

    if _model_wrapper.IsSteppable():
        raise Exception("You need to use the ModelWrapper directly because this model is steppable, which means the input is provided by a callback method")
        
    inputVector = FloatVector(inputData)
    output = _model_wrapper.Predict(inputVector)
    return np.array(output)

def reset():
    model_Reset()


%}
#endif // defined(SWIGPYTHON)

%include "model.i.h"

%inline %{
  TensorShape get_default_input_shape() {
    TensorShape  s;
    model_GetInputShape(0, &s);
    return s;
  }
  TensorShape get_default_output_shape() {
    TensorShape  s;
    model_GetOutputShape(0, &s);
    return s;
  }
%}

%pythoncode %{
  
def TensorShape_Size(self):
    return self.rows * self.columns * self.channels

TensorShape.Size = TensorShape_Size

%}

