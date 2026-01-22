from typing import Dict, Any, Optional
from shevchenko.extension import ShevchenkoExtension, ExtensionContext, AfterInflectHook
from shevchenko.language import GrammaticalCase
from shevchenko.contracts import DeclensionInput, DeclensionOutput
from .military_inflector import MilitaryInflector

def _create_after_inflect_hook(military_inflector: MilitaryInflector) -> AfterInflectHook:
    def hook(grammatical_case: GrammaticalCase, input_data: DeclensionInput) -> DeclensionOutput:
        output: DeclensionOutput = {}
        
        military_rank = input_data.get('militaryRank')
        if military_rank:
            output['militaryRank'] = military_inflector.inflect(
                military_rank,
                grammatical_case,
                'militaryRank'
            )

        military_appointment = input_data.get('militaryAppointment')
        if military_appointment:
            output['militaryAppointment'] = military_inflector.inflect(
                military_appointment,
                grammatical_case,
                'militaryAppointment'
            )
            
        return output
    return hook

def military_extension(context: ExtensionContext) -> ShevchenkoExtension:
    word_inflector = context.get('wordInflector')
    
    if word_inflector is None:
        # Fallback to importing default if not provided in context
        from shevchenko.word_declension.bootstrap import word_inflector as default_inflector
        word_inflector = default_inflector

    inflector = MilitaryInflector(word_inflector)

    return ShevchenkoExtension(
        fieldNames=['militaryRank', 'militaryAppointment'],
        afterInflect=_create_after_inflect_hook(inflector)
    )
