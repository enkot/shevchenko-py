from typing import Any, List, Callable, Dict, Optional
from shevchenko.contracts import DeclensionInput, DeclensionOutput
from shevchenko.language import GrammaticalCase

ExtensionContext = Dict[str, Any]  # Placeholder for now until wordInflector is ready
FieldName = str

# defined callback as sync
AfterInflectHook = Callable[[GrammaticalCase, DeclensionInput], DeclensionOutput]

class ShevchenkoExtension:
    fieldNames: List[FieldName]
    afterInflect: Optional[AfterInflectHook] = None

    def __init__(self, fieldNames: List[FieldName], afterInflect: Optional[AfterInflectHook] = None):
        self.fieldNames = fieldNames
        self.afterInflect = afterInflect

ExtensionFactory = Callable[[ExtensionContext], ShevchenkoExtension]

_registered_extensions: List[ShevchenkoExtension] = []

def register_extension(extension_factory: ExtensionFactory) -> None:
    # TODO: Pass real context
    # from shevchenko.word_declension.bootstrap import word_inflector
    context = {'wordInflector': None} 
    extension = extension_factory(context)
    _registered_extensions.append(extension)

def get_custom_field_names() -> List[FieldName]:
    field_names = []
    for extension in _registered_extensions:
        field_names.extend(extension.fieldNames)
    return field_names

def after_inflect(grammatical_case: GrammaticalCase, input_data: DeclensionInput) -> DeclensionOutput:
    output: DeclensionOutput = {}
    for extension in _registered_extensions:
        if extension.afterInflect:
            custom_output = extension.afterInflect(grammatical_case, input_data)
            if custom_output:
                output.update(custom_output)
    return output
