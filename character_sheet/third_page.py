from cgi_simple import (
    div, ensure_valid_attributes_and_contents, flex_col, flex_row, flex_wrapper,
    labeled_text_input, text_input,
)

def create_page():
    return flex_row({'class': 'third-page'}, [
        flex_col({'class': 'sidebar'}, [
            feats_summary(),
            proficiencies(),
            inventory(),
            adventuring(),
            flex_col([
                flex_wrapper(div({'class': 'section-header'}, 'Experience')),
                div(text_input()),
            ]),
            flex_col([
                flex_wrapper(div({'class': 'section-header'}, 'Wealth')),
                div(text_input()),
            ]),
        ]),
        flex_col({'class': 'main-body'}, [
            equipment(),
            abilities_summary(),
            description(),
        ]),
    ])

def feats_summary():
    return flex_col({'class': 'feats-summary'}, [
        flex_row({'class': 'summary-header'}, [
            div({'class': 'summary-header-level section-header'}, 'Lvl'),
            div({'class': 'summary-header-name section-header'}, 'Feats'),
        ]),
        "".join([summary_row(i) for i in [1, 1, 3, 6, 10]]),
    ])

def abilities_summary():
    return flex_col({'class': 'abilities'}, [
        flex_wrapper(div({'class': 'section-header'}, 'Abilities')),
        *[
            flex_row([
                labeled_text_input('Name', f'ability-name-{i}', {'class': 'ability-name'}),
                labeled_text_input('Effects', f'ability-effects-{i}', {'class': 'ability-effects'}),
            ])
            for i in range(12)
        ],
    ])

def summary_row(level=None):
    return flex_row({'class': 'summary-row'}, [
        div({'class': 'summary-row-level'}, text_input({
            'value': level,
        })),
        div({'class': 'summary-row-name'}, text_input()),
    ])

def proficiencies():
    return flex_col({'class': 'proficiencies'}, [
        flex_wrapper(div({'class': 'section-header'}, 'Proficiencies')),
        labeled_text_input('Armor', 'prof-armor'),
        labeled_text_input('Weapons', 'prof-weapons'),
        text_input(),
        labeled_text_input('Languages', 'prof-languages'),
    ])

def subsection_header(attributes=None, contents=None):
    attributes, contents = ensure_valid_attributes_and_contents(attributes, contents)
    attributes['class'] = 'subsection-header ' + attributes.get('class', '')
    return flex_col(attributes, contents)

def equipment():
    return flex_col({'class': 'equipment'}, [
        flex_wrapper(div({'class': 'section-header'}, 'Equipment')),
        *[
            flex_row([
                labeled_text_input('Name', f'equipment-name-{i}', {'class': 'equipment-name'}),
                labeled_text_input('Effects', f'equipment-effects-{i}', {'class': 'equipment-effects'}),
            ])
            for i in range(6)
        ],
    ])

def inventory():
    return div({'class': 'inventory'}, [
        flex_wrapper(div({'class': 'section-header'}, 'Inventory')),
        *[
            text_input() for i in range(14)
        ]
    ])

def misc_equipment(body_slot, body_slot_html=None):
    if body_slot_html is None:
        body_slot_html = body_slot.lower()
    return flex_row({'class': body_slot_html}, [
        subsection_header(body_slot),
        labeled_text_input('Name', body_slot_html + '-name', {'class': 'equipment-name'}),
        labeled_text_input('Special', body_slot_html + '-special', {'class': 'equipment-special'}),
    ])

def adventuring():
    return flex_row({'class': 'adventuring'}, [
        flex_col({'class': 'misc'}, [
            flex_wrapper(div({'class': 'section-header'}, 'Weight Limits')),
            flex_row({'class': 'weight-limits'}, [
                labeled_text_input('Normal', 'weight-normal'),
                labeled_text_input('Overloaded', 'weight-overloaded'),
            ]),
            flex_row({'class': 'weight-limits'}, [
                labeled_text_input('Max', 'weight-max'),
                labeled_text_input('Push/Drag', 'weight-push-drag'),
            ]),
        ]),
    ])

def description():
    return flex_col({'class': 'description'}, [
        div({'class': 'section-header'}, 'Personality and Description'),
        "".join([
            div({'class': 'description-row'}, text_input()) for i in range(5)
        ]),
    ])
