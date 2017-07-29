from generation.util import join

class MagicItem(object):

    @classmethod
    def automatic_materials(cls, material_type):
        return {
            'amulet': ['jewelry'],
            'belt': ['leather', 'textiles'],
            'boot': ['bone', 'leather', 'metal'],
            'bracer': ['bone', 'leather', 'metal', 'wood'],
            'cloak': ['textiles'],
            'crown': ['bone', 'metal'],
            'gauntlet': ['bone', 'metal', 'wood'],
            'glove': ['leather'],
            'mask': ['textiles'],
            'ring': ['bone', 'jewelry', 'metal', 'wood'],
        }[material_type]

    def __init__(
            self,
            description,
            level,
            name,
            tags,
            armor_type=None,
            effects=None,
            material_type=None,
            materials=None,
            targeting=None,
    ):
        self.description = description
        self.level = level
        self.name = name
        self.tags = tags

        self.armor_type = armor_type
        self.effects = effects
        try:
            self.materials = materials or MagicItem.automatic_materials(material_type)
        except KeyError:
            raise Exception(f"Item '{self.name}' has unknown material_type {material_type}")
        self.targeting = targeting

    def latex_ability(self):
        if self.effects or self.targeting:
            return f"""
                \\begin<spellcontent>
                    {self.targeting or ""}
                    {self.effects or ""}
                \\end<spellcontent>
            """
        else:
            return None

    def latex_tags(self):
        return ', '.join([f"\\glossterm<{tag}>" for tag in sorted(self.tags)])

    def latex(self):
        return join(
            f"""
                \\begin<multicols><2>
                    \\lowercase<\\hypertarget<item:{self.name}><>>\\label<item:{self.name}>
                    \\hypertarget<item:{self.name}><\\subsection<{self.name}>>
                    \\columnbreak%
                    \\begin<flushright>
                        \\large\\textbf<\\nth<{self.level}> Level>
                    \\end<flushright>
                \\end<multicols>
                \\vspace<-1.5em>  % Correct weird spacing from multicols
                {self.description}
            """,
            self.latex_ability(),
            f"""
                \\parhead*<Tags> {self.latex_tags()}
                \\parhead*<Materials> {', '.join(sorted(self.materials))}
            """,
            """
                \\parhead*<Armor Type> {self.armor_type}
            """ if self.armor_type else None,
        )