valid_tags = set([
    'Acid',
    'Air',
    'Attune (ritual)',
    'Attune (ritual; see text)',
    'Attune (self)',
    'Attune (target)',
    'Auditory',
    'Cold',
    'Compulsion',
    'Creation',
    'Curse',
    'Emotion',
    'Detection',
    'Earth',
    'Electricity',
    'Fire',
    'Flesh',
    'Life',
    'Light',
    'Manifestation',
    'Mind',
    'Mystic',
    'Physical',
    'Planar',
    'Poison',
    'Scrying',
    '(see text)',
    'Sensation',
    'Shaping',
    'Shielding',
    'Sizing',
    'Speech',
    'Subtle',
    'Sustain (standard)',
    'Sustain (minor)',
    'Swift',
    'Teleportation',
    'Temporal',
    'Trap',
    'Visual',
    'Water',
])

def glosstermify(tag):
    if tag == '(see text)':
        return tag
    elif ' ' in tag:
        split_tag = tag.split()
        return f"\\glossterm<{split_tag[0]}> {' '.join(split_tag[1:])}"
    else:
        return f"\\glossterm<{tag}>"

def is_valid_tag(tag):
    return tag in valid_tags
