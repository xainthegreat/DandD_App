from PyQt6.QtWidgets import QWidget, QComboBox, QListWidget, QLCDNumber, QSpinBox, QPushButton, QLineEdit, \
    QPlainTextEdit, QInputDialog, QFileDialog
from PyQt6 import uic
import sys
from Final.FileManager import FileManager


class UI(QWidget):
    '''
    class that creates a gui for creating a new D&D character
    '''
    def __init__(self):
        super().__init__()

        # loading the ui file with uic module
        uic.loadUi("newcharacterform_simple.ui", self)

        # add save, load, and cancel buttons
        self.add_control_buttons()
        self.add_playerinfo_children()
        self.add_addtolist_buttons()

        # add everything related to the attributes
        self.cur_str = self.cur_dex = self.cur_con = self.cur_int = self.cur_wis = self.cur_cha = 'Select One'
        self.set_attribute_events()
        self.update_totals()

    def add_control_buttons(self):
        '''
        adds utility button widgets; save,load,edit,exit
        :return:
        none
        '''
        self.save_button = self.findChild(QPushButton, "saveButton")
        self.save_button.clicked.connect(self.save_character)

        self.load_button = self.findChild(QPushButton, "loadButton")
        self.load_button.clicked.connect(self.load_character)

        self.cancel_button = self.findChild(QPushButton, "cancelButton")
        self.cancel_button.clicked.connect(self.back_to_main)

        self.is_editable = True
        self.edit_button = self.findChild(QPushButton, "editBaseStatsButton")
        self.edit_button.clicked.connect(self.enable_disable_edit)

    def add_playerinfo_children(self):
        '''
        adds all the player info widgets
        :return:
        none
        '''
        self.player_name_line = self.findChild(QLineEdit, "playerNameTextBox")
        self.character_name_line = self.findChild(QLineEdit, "characterNameTextBox")
        self.race_combo = self.findChild(QComboBox, "raceComboBox")
        self.class_combo = self.findChild(QComboBox, "classComboBox")
        self.background_combo = self.findChild(QComboBox, "backgroundComboBox")
        self.alignment_combo = self.findChild(QComboBox, "alignmentComboBox")
        self.biography_text = self.findChild(QPlainTextEdit, "biographyTextEdit")
        self.level_spinbox = self.findChild(QSpinBox, "levelSpinBox")
        self.proficiencies_languages_list = self.findChild(QListWidget, "proficienciesLanguagesListWidget")
        self.attacks_spells_list = self.findChild(QListWidget, "attacksSpellsListWidget")
        self.equipment_list = self.findChild(QListWidget, "equipmentListWidget")
        self.features_traits_list = self.findChild(QListWidget, "featuresTraitsListWidget")
        self.personality_traits_list = self.findChild(QListWidget, "peronalitytraitListWidget")
        self.ideals_list = self.findChild(QListWidget, "idealsListWidget")
        self.bonds_list = self.findChild(QListWidget, "bondsListWidget")
        self.flaws_list = self.findChild(QListWidget, "flawsListWidget")

    def add_addtolist_buttons(self):
        '''
        adds all buttons and events for adding and remove items from all list widgets
        :return:
        none
        '''
        self.proficiencies_languages_addButton = self.findChild(QPushButton, "addProficiencyButton")
        self.proficiencies_languages_addButton.clicked.connect(
            lambda state, x=True: self.update_proficiencies_languages(x))
        self.proficiencies_languages_removeButton = self.findChild(QPushButton, "removeProficiencyButton")
        self.proficiencies_languages_removeButton.clicked.connect(
            lambda state, x=False: self.update_proficiencies_languages(x))

        self.attacks_spells_addButton = self.findChild(QPushButton, "addAttackandspellsButton")
        self.attacks_spells_addButton.clicked.connect(lambda state, x=True: self.update_attacks_spells(x))
        self.attacks_spells_removeButton = self.findChild(QPushButton, "removeAttackandspellsButton")
        self.attacks_spells_removeButton.clicked.connect(lambda state, x=False: self.update_attacks_spells(x))

        self.equipment_addButton = self.findChild(QPushButton, "addEquipmentButton")
        self.equipment_addButton.clicked.connect(lambda state, x=True: self.update_equipment(x))
        self.equipment_removeButton = self.findChild(QPushButton, "removeEquipmentButton")
        self.equipment_removeButton.clicked.connect(lambda state, x=False: self.update_equipment(x))

        self.features_traits_addButton = self.findChild(QPushButton, "addTraitandfeaturesButton")
        self.features_traits_addButton.clicked.connect(lambda state, x=True: self.update_features_traits(x))
        self.features_traits_removeButton = self.findChild(QPushButton, "removeTraitandfeaturesButton")
        self.features_traits_removeButton.clicked.connect(lambda state, x=False: self.update_features_traits(x))

        self.personality_traits_addButton = self.findChild(QPushButton, "addPersonalitytraitButton")
        self.personality_traits_addButton.clicked.connect(lambda state, x=True: self.update_personality_traits(x))
        self.personality_traits_removeButton = self.findChild(QPushButton, "removePersonalitytraitButton")
        self.personality_traits_removeButton.clicked.connect(lambda state, x=False: self.update_personality_traits(x))

        self.ideals_addButton = self.findChild(QPushButton, "addIdealsButton")
        self.ideals_addButton.clicked.connect(lambda state, x=True: self.update_ideals(x))
        self.ideals_removeButton = self.findChild(QPushButton, "removeIdealsButton")
        self.ideals_removeButton.clicked.connect(lambda state, x=False: self.update_ideals(x))

        self.bonds_addButton = self.findChild(QPushButton, "addBondsButton")
        self.bonds_addButton.clicked.connect(lambda state, x=True: self.update_bonds(x))
        self.bonds_removeButton = self.findChild(QPushButton, "removeBondsButton")
        self.bonds_removeButton.clicked.connect(lambda state, x=False: self.update_bonds(x))

        self.flaws_addButton = self.findChild(QPushButton, "addFlawsButton")
        self.flaws_addButton.clicked.connect(lambda state, x=True: self.update_flaws(x))
        self.flaws_removeButton = self.findChild(QPushButton, "removeFlawsButton")
        self.flaws_removeButton.clicked.connect(lambda state, x=False: self.update_flaws(x))

    def set_attribute_events(self):
        '''
        adds all attribute based widgets and events attached to those widgets
        :return:
        none
        '''
        self.strength_combo = self.findChild(QComboBox, "strengthComboBox")
        self.dexterity_combo = self.findChild(QComboBox, "dexterityComboBox")
        self.constitution_combo = self.findChild(QComboBox, "constitutionComboBox")
        self.intelligence_combo = self.findChild(QComboBox, "intelligenceComboBox")
        self.wisdom_combo = self.findChild(QComboBox, "wisdomComboBox")
        self.charisma_combo = self.findChild(QComboBox, "charismaComboBox")
        self.strength_combo.currentTextChanged.connect(self.strength_combo_changed)
        self.dexterity_combo.currentTextChanged.connect(self.dexterity_combo_changed)
        self.constitution_combo.currentTextChanged.connect(self.constitution_combo_changed)
        self.intelligence_combo.currentTextChanged.connect(self.intelligence_combo_changed)
        self.wisdom_combo.currentTextChanged.connect(self.wisdom_combo_changed)
        self.charisma_combo.currentTextChanged.connect(self.charisma_combo_changed)

        self.hp_bonus_spinbox = self.findChild(QSpinBox, "hpBonusesSpinBox")
        self.strength_race_spinbox = self.findChild(QSpinBox, "strengthRaceSpinBox")
        self.dexterity_race_spinbox = self.findChild(QSpinBox, "dexterityRaceSpinBox")
        self.constitution_race_spinbox = self.findChild(QSpinBox, "constitutionRaceSpinBox")
        self.intelligence_race_spinbox = self.findChild(QSpinBox, "intelligenceRaceSpinBox")
        self.wisdom_race_spinbox = self.findChild(QSpinBox, "wisdomRaceSpinBox")
        self.charisma_race_spinbox = self.findChild(QSpinBox, "charismaRaceSpinBox")
        self.hp_bonus_spinbox.valueChanged.connect(self.update_totals)
        self.strength_race_spinbox.valueChanged.connect(self.update_totals)
        self.dexterity_race_spinbox.valueChanged.connect(self.update_totals)
        self.constitution_race_spinbox.valueChanged.connect(self.update_totals)
        self.intelligence_race_spinbox.valueChanged.connect(self.update_totals)
        self.wisdom_race_spinbox.valueChanged.connect(self.update_totals)
        self.charisma_race_spinbox.valueChanged.connect(self.update_totals)

        self.hp_class_spinbox = self.findChild(QSpinBox, "hpSpinBox")
        self.strength_class_spinbox = self.findChild(QSpinBox, "strengthClassSpinBox")
        self.dexterity_class_spinbox = self.findChild(QSpinBox, "dexterityClassSpinBox")
        self.constitution_class_spinbox = self.findChild(QSpinBox, "constitutionClassSpinBox")
        self.intelligence_class_spinbox = self.findChild(QSpinBox, "intelligenceClassSpinBox")
        self.wisdom_class_spinbox = self.findChild(QSpinBox, "wisdomClassSpinBox")
        self.charisma_class_spinbox = self.findChild(QSpinBox, "charismaClassSpinBox")
        self.hp_class_spinbox.valueChanged.connect(self.update_totals)
        self.strength_class_spinbox.valueChanged.connect(self.update_totals)
        self.dexterity_class_spinbox.valueChanged.connect(self.update_totals)
        self.constitution_class_spinbox.valueChanged.connect(self.update_totals)
        self.intelligence_class_spinbox.valueChanged.connect(self.update_totals)
        self.wisdom_class_spinbox.valueChanged.connect(self.update_totals)
        self.charisma_class_spinbox.valueChanged.connect(self.update_totals)

        self.hp_level_spinbox = self.findChild(QSpinBox, "hpLevelupSpinBox")
        self.strength_level_spinbox = self.findChild(QSpinBox, "strengthLevelupSpinBox")
        self.dexterity_level_spinbox = self.findChild(QSpinBox, "dexterityLevelupSpinBox")
        self.constitution_level_spinbox = self.findChild(QSpinBox, "constitutionLevelupSpinBox")
        self.intelligence_level_spinbox = self.findChild(QSpinBox, "intelligenceLevelupSpinBox")
        self.wisdom_level_spinbox = self.findChild(QSpinBox, "wisdomLevelupSpinBox")
        self.charisma_level_spinbox = self.findChild(QSpinBox, "charismaLevelupSpinBox")
        self.hp_level_spinbox.valueChanged.connect(self.update_totals)
        self.strength_level_spinbox.valueChanged.connect(self.update_totals)
        self.dexterity_level_spinbox.valueChanged.connect(self.update_totals)
        self.constitution_level_spinbox.valueChanged.connect(self.update_totals)
        self.intelligence_level_spinbox.valueChanged.connect(self.update_totals)
        self.wisdom_level_spinbox.valueChanged.connect(self.update_totals)
        self.charisma_level_spinbox.valueChanged.connect(self.update_totals)

        self.hp_total_LCD = self.findChild(QLCDNumber, "hpTotalNumber")
        self.strength_total_LCD = self.findChild(QLCDNumber, "strengthTotalNumber")
        self.dexterity_total_LCD = self.findChild(QLCDNumber, "dexterityTotalNumber")
        self.constitution_total_LCD = self.findChild(QLCDNumber, "constitutionTotalNumber")
        self.intelligence_total_LCD = self.findChild(QLCDNumber, "intelligenceTotalNumber")
        self.wisdom_total_LCD = self.findChild(QLCDNumber, "wisdomTotalNumber")
        self.charisma_total_LCD = self.findChild(QLCDNumber, "charismaTotalNumber")

        self.strength_modifier_LCD = self.findChild(QLCDNumber, "strengthModifierNumber")
        self.dexterity_modifier_LCD = self.findChild(QLCDNumber, "dexterityModifierNumber")
        self.constitution_modifier_LCD = self.findChild(QLCDNumber, "constitutionModifierNumber")
        self.constitution_modifier_hp_LCD = self.findChild(QLCDNumber, "hpConstitutionModifierNumber")
        self.intelligence_modifier_LCD = self.findChild(QLCDNumber, "intelligenceModifierNumber")
        self.wisdom_modifier_LCD = self.findChild(QLCDNumber, "wisdomModifierNumber")
        self.charisma_modifier_LCD = self.findChild(QLCDNumber, "charismaModifierNumber")

    def save_character(self):
        '''
        sends all the completed fields to be saved to a .json file
        sets is_enabled to false
        :return:
        none
        '''
        character_data = {
            "Player Info": {
                "Player Name": self.player_name_line.text(),
                "Character Name": self.character_name_line.text(),
                "Race": self.race_combo.currentText(),
                "Class": self.class_combo.currentText(),
                "Background": self.background_combo.currentText(),
                "Alignment": self.alignment_combo.currentText(),
                "Biography": self.biography_text.toPlainText(),
                "Level": self.level_spinbox.value()
            },
            "Attributes": {
                "Class Bonus HP": self.hp_class_spinbox.value(),
                "Other Bonus HP": self.hp_bonus_spinbox.value(),
                "Level-Up Bonus HP": self.hp_level_spinbox.value(),
                "Base Strength": self.strength_combo.currentText(),
                "Race Bonus Strength": self.strength_race_spinbox.value(),
                "Class Bonus Strength": self.strength_class_spinbox.value(),
                "Level-Up Bonus Strength": self.strength_level_spinbox.value(),
                "Base Dexterity": self.dexterity_combo.currentText(),
                "Race Bonus Dexterity": self.dexterity_race_spinbox.value(),
                "Class Bonus Dexterity": self.dexterity_class_spinbox.value(),
                "Level-Up Bonus Dexterity": self.dexterity_level_spinbox.value(),
                "Base Constitution": self.constitution_combo.currentText(),
                "Race Bonus Constitution": self.constitution_race_spinbox.value(),
                "Class Bonus Constitution": self.constitution_class_spinbox.value(),
                "Level-Up Bonus Constitution": self.constitution_level_spinbox.value(),
                "Base Intelligence": self.intelligence_combo.currentText(),
                "Race Bonus Intelligence": self.intelligence_race_spinbox.value(),
                "Class Bonus Intelligence": self.intelligence_class_spinbox.value(),
                "Level-Up Bonus Intelligence": self.intelligence_level_spinbox.value(),
                "Base Wisdom": self.wisdom_combo.currentText(),
                "Race Bonus Wisdom": self.wisdom_race_spinbox.value(),
                "Class Bonus Wisdom": self.wisdom_class_spinbox.value(),
                "Level-Up Bonus Wisdom": self.wisdom_level_spinbox.value(),
                "Base Charisma": self.charisma_combo.currentText(),
                "Race Bonus Charisma": self.charisma_race_spinbox.value(),
                "Class Bonus Charisma": self.charisma_class_spinbox.value(),
                "Level-Up Bonus Charisma": self.charisma_level_spinbox.value()
            },
            "Proficiencies and Languages": [self.proficiencies_languages_list.item(x).text() for x in
                                            range(self.proficiencies_languages_list.count())],
            "Attacks and Spells": [self.attacks_spells_list.item(x).text() for x in
                                   range(self.attacks_spells_list.count())],
            "Equipment": [self.equipment_list.item(x).text() for x in range(self.equipment_list.count())],
            "Features and Traits": [self.features_traits_list.item(x).text() for x in
                                    range(self.features_traits_list.count())],
            "Personality Traits": [self.personality_traits_list.item(x).text() for x in
                                   range(self.personality_traits_list.count())],
            "Ideals": [self.ideals_list.item(x).text() for x in range(self.ideals_list.count())],
            "Bonds": [self.bonds_list.item(x).text() for x in range(self.bonds_list.count())],
            "Flaws": [self.flaws_list.item(x).text() for x in range(self.flaws_list.count())]
        }

        FileManager.save_to_json(character_data)

        if self.is_editable:
            self.enable_disable_edit()

    def load_character(self):
        '''
        opens file dialog box and pushes path of selected .json to load the data into the window
        sets is_enabled to false
        :return:
        none
        '''
        path = QFileDialog.getOpenFileName(self, 'Open a file', '', 'All Files (*.*)')
        if path != ('', ''):
            data = FileManager.load_from_json(path[0])

            self.player_name_line.setText(str(data['Player Info']['Player Name']))
            self.character_name_line.setText(str(data['Player Info']['Character Name']))
            self.race_combo.setCurrentText(data['Player Info']['Race'])
            self.class_combo.setCurrentText(data['Player Info']['Class'])
            self.background_combo.setCurrentText(data['Player Info']['Background'])
            self.alignment_combo.setCurrentText(data['Player Info']['Alignment'])
            self.biography_text.setPlainText(data['Player Info']['Biography'])
            self.level_spinbox.setValue(int(data['Player Info']['Level']))

            self.hp_class_spinbox.setValue(int(data['Attributes']['Class Bonus HP']))
            self.hp_bonus_spinbox.setValue(int(data['Attributes']['Other Bonus HP']))
            self.hp_level_spinbox.setValue(int(data['Attributes']['Level-Up Bonus HP']))
            self.strength_combo.setCurrentText(str(data['Attributes']['Base Strength']))
            self.strength_race_spinbox.setValue(int(data['Attributes']['Race Bonus Strength']))
            self.strength_class_spinbox.setValue(int(data['Attributes']['Class Bonus Strength']))
            self.strength_level_spinbox.setValue(int(data['Attributes']['Level-Up Bonus Strength']))
            self.dexterity_combo.setCurrentText(str(data['Attributes']['Base Dexterity']))
            self.dexterity_race_spinbox.setValue(int(data['Attributes']['Race Bonus Dexterity']))
            self.dexterity_class_spinbox.setValue(int(data['Attributes']['Class Bonus Dexterity']))
            self.dexterity_level_spinbox.setValue(int(data['Attributes']['Level-Up Bonus Dexterity']))
            self.constitution_combo.setCurrentText(str(data['Attributes']['Base Constitution']))
            self.constitution_race_spinbox.setValue(int(data['Attributes']['Race Bonus Constitution']))
            self.constitution_class_spinbox.setValue(int(data['Attributes']['Class Bonus Constitution']))
            self.constitution_level_spinbox.setValue(int(data['Attributes']['Level-Up Bonus Constitution']))
            self.intelligence_combo.setCurrentText(str(data['Attributes']['Base Intelligence']))
            self.intelligence_race_spinbox.setValue(int(data['Attributes']['Race Bonus Intelligence']))
            self.intelligence_class_spinbox.setValue(int(data['Attributes']['Class Bonus Intelligence']))
            self.intelligence_level_spinbox.setValue(int(data['Attributes']['Level-Up Bonus Intelligence']))
            self.wisdom_combo.setCurrentText(str(data['Attributes']['Base Wisdom']))
            self.wisdom_race_spinbox.setValue(int(data['Attributes']['Race Bonus Wisdom']))
            self.wisdom_class_spinbox.setValue(int(data['Attributes']['Class Bonus Wisdom']))
            self.wisdom_level_spinbox.setValue(int(data['Attributes']['Level-Up Bonus Wisdom']))
            self.charisma_combo.setCurrentText(str(data['Attributes']['Base Charisma']))
            self.charisma_race_spinbox.setValue(int(data['Attributes']['Race Bonus Charisma']))
            self.charisma_class_spinbox.setValue(int(data['Attributes']['Class Bonus Charisma']))
            self.charisma_level_spinbox.setValue(int(data['Attributes']['Level-Up Bonus Charisma']))

            self.proficiencies_languages_list.addItems(list(data['Proficiencies and Languages']))
            self.attacks_spells_list.addItems(list(data['Attacks and Spells']))
            self.equipment_list.addItems(list(data['Equipment']))
            self.features_traits_list.addItems(list(data['Features and Traits']))
            self.personality_traits_list.addItems(list(data['Personality Traits']))
            self.ideals_list.addItems(list(data['Ideals']))
            self.bonds_list.addItems(list(data['Bonds']))
            self.flaws_list.addItems(list(data['Flaws']))

            if self.is_editable:
                self.enable_disable_edit()

    def back_to_main(self):
        '''
        closes the window and exits the program
        :return:
        none
        '''
        sys.exit()  ## todo make a main page and have button send back

    def enable_disable_edit(self):
        '''
        enables or disables the fields that are set when first creating a character
        :return:
        none
        '''
        if self.is_editable:
            self.is_editable = False
        else:
            self.is_editable = True

        self.player_name_line.setEnabled(self.is_editable)
        self.character_name_line.setEnabled(self.is_editable)
        self.biography_text.setEnabled(self.is_editable)
        self.race_combo.setEnabled(self.is_editable)
        self.class_combo.setEnabled(self.is_editable)
        self.background_combo.setEnabled(self.is_editable)
        self.alignment_combo.setEnabled(self.is_editable)
        self.hp_class_spinbox.setEnabled(self.is_editable)
        self.hp_bonus_spinbox.setEnabled(self.is_editable)
        self.strength_combo.setEnabled(self.is_editable)
        self.strength_race_spinbox.setEnabled(self.is_editable)
        self.strength_class_spinbox.setEnabled(self.is_editable)
        self.dexterity_combo.setEnabled(self.is_editable)
        self.dexterity_race_spinbox.setEnabled(self.is_editable)
        self.dexterity_class_spinbox.setEnabled(self.is_editable)
        self.constitution_combo.setEnabled(self.is_editable)
        self.constitution_race_spinbox.setEnabled(self.is_editable)
        self.constitution_class_spinbox.setEnabled(self.is_editable)
        self.intelligence_combo.setEnabled(self.is_editable)
        self.intelligence_race_spinbox.setEnabled(self.is_editable)
        self.intelligence_class_spinbox.setEnabled(self.is_editable)
        self.wisdom_combo.setEnabled(self.is_editable)
        self.wisdom_race_spinbox.setEnabled(self.is_editable)
        self.wisdom_class_spinbox.setEnabled(self.is_editable)
        self.charisma_combo.setEnabled(self.is_editable)
        self.charisma_race_spinbox.setEnabled(self.is_editable)
        self.charisma_class_spinbox.setEnabled(self.is_editable)

    def update_proficiencies_languages(self, operation):
        '''
        adds or removes item from proficiency and languages list widget
        :param operation:
        Boolean; true if adding, false if removing
        :return:
        none
        '''
        if operation:
            text, ok = QInputDialog.getText(self, 'Add Proficiency or Language',
                                            'What is your new proficiency or language?')
            if ok:
                self.proficiencies_languages_list.addItem(str(text))
        else:
            try:
                self.proficiencies_languages_list.takeItem(
                    self.proficiencies_languages_list.row(self.proficiencies_languages_list.currentItem()))
            except:
                print('Could Not remove items using update_proficiencies_languages')

    def update_attacks_spells(self, operation):
        '''
        adds or removes item from attacks and spells list widget
        :param operation:
        Boolean; true if adding, false if removing
        :return:
        none
        '''
        if operation:
            text, ok = QInputDialog.getText(self, 'Add Attack or Spell', 'What is your new attack or spell?')
            if ok:
                self.attacks_spells_list.addItem(str(text))
        else:
            try:
                self.attacks_spells_list.takeItem(self.attacks_spells_list.row(self.attacks_spells_list.currentItem()))
            except:
                print('Could Not remove items using update_attacks_spells')

    def update_equipment(self, operation):
        '''
        adds or removes item from equipment list widget
        :param operation:
        Boolean; true if adding, false if removing
        :return:
        none
        '''
        if operation:
            text, ok = QInputDialog.getText(self, 'Add Equipment or Item', 'What is your new equipment or item?')
            if ok:
                self.equipment_list.addItem(str(text))
        else:
            try:
                self.equipment_list.takeItem(self.equipment_list.row(self.equipment_list.currentItem()))
            except:
                print('Could Not remove items using update_equipment')

    def update_features_traits(self, operation):
        '''
        adds or removes item from features and traits list widget
        :param operation:
        Boolean; true if adding, false if removing
        :return:
        none
        '''
        if operation:
            text, ok = QInputDialog.getText(self, 'Add Feature or Trait', 'What is your new feature or trait?')
            if ok:
                self.features_traits_list.addItem(str(text))
        else:
            try:
                self.features_traits_list.takeItem(
                    self.features_traits_list.row(self.features_traits_list.currentItem()))
            except:
                print('Could Not remove items using update_features_traits')

    def update_personality_traits(self, operation):
        '''
        adds or removes item from personality trait list widget
        :param operation:
        Boolean; true if adding, false if removing
        :return:
        none
        '''
        if operation:
            text, ok = QInputDialog.getText(self, 'Add Personality Trait', 'What is your new personality trait?')
            if ok:
                self.personality_traits_list.addItem(str(text))
        else:
            try:
                self.personality_traits_list.takeItem(
                    self.personality_traits_list.row(self.personality_traits_list.currentItem()))
            except:
                print('Could Not remove items using update_personality_traits')

    def update_ideals(self, operation):
        '''
        adds or removes item from ideal list widget
        :param operation:
        Boolean; true if adding, false if removing
        :return:
        none
        '''
        if operation:
            text, ok = QInputDialog.getText(self, 'Add Ideal', 'What is your new ideal?')
            if ok:
                self.ideals_list.addItem(str(text))
        else:
            try:
                self.ideals_list.takeItem(self.ideals_list.row(self.ideals_list.currentItem()))
            except:
                print('Could Not remove items using update_ideals')

    def update_bonds(self, operation):
        '''
        adds or removes item from bond list widget
        :param operation:
        Boolean; true if adding, false if removing
        :return:
        none
        '''
        if operation:
            text, ok = QInputDialog.getText(self, 'Add Bond', 'What is your new bond?')
            if ok:
                self.bonds_list.addItem(str(text))
        else:
            try:
                self.bonds_list.takeItem(self.bonds_list.row(self.bonds_list.currentItem()))
            except:
                print('Could Not remove items using update_bonds')

    def update_flaws(self, operation):
        '''
        adds or removes item from flaw list widget
        :param operation:
        Boolean; true if adding, false if removing
        :return:
        none
        '''
        if operation:
            text, ok = QInputDialog.getText(self, 'Add Flaw', 'What is your new flaw?')
            if ok:
                self.flaws_list.addItem(str(text))
        else:
            self.flaws_list.takeItem(self.flaws_list.row(self.flaws_list.currentItem()))

    def strength_combo_changed(self):
        '''
        if previous selection was a number add it back to all attributes.
        update the current selection and remove from all other attributes if a number
        :return:
        none
        '''
        if self.cur_str != 'Select One':
            self.dexterity_combo.addItem(self.cur_str)
            self.constitution_combo.addItem(self.cur_str)
            self.intelligence_combo.addItem(self.cur_str)
            self.wisdom_combo.addItem(self.cur_str)
            self.charisma_combo.addItem(self.cur_str)

        self.cur_str = self.strength_combo.currentText()

        if self.cur_str != 'Select One':
            try:
                self.dexterity_combo.removeItem(self.dexterity_combo.findText(self.cur_str))
                self.constitution_combo.removeItem(self.constitution_combo.findText(self.cur_str))
                self.intelligence_combo.removeItem(self.intelligence_combo.findText(self.cur_str))
                self.wisdom_combo.removeItem(self.wisdom_combo.findText(self.cur_str))
                self.charisma_combo.removeItem(self.charisma_combo.findText(self.cur_str))
            except:
                print('attribute update error')

        self.update_totals()

    def dexterity_combo_changed(self):
        '''
        if previous selection was a number add it back to all attributes.
        update the current selection and remove from all other attributes if a number
        :return:
        none
        '''
        if self.cur_dex != 'Select One':
            self.strength_combo.addItem(self.cur_dex)
            self.constitution_combo.addItem(self.cur_dex)
            self.intelligence_combo.addItem(self.cur_dex)
            self.wisdom_combo.addItem(self.cur_dex)
            self.charisma_combo.addItem(self.cur_dex)

        self.cur_dex = self.dexterity_combo.currentText()

        if self.cur_dex != 'Select One':
            try:
                self.strength_combo.removeItem(self.strength_combo.findText(self.cur_dex))
                self.constitution_combo.removeItem(self.constitution_combo.findText(self.cur_dex))
                self.intelligence_combo.removeItem(self.intelligence_combo.findText(self.cur_dex))
                self.wisdom_combo.removeItem(self.wisdom_combo.findText(self.cur_dex))
                self.charisma_combo.removeItem(self.charisma_combo.findText(self.cur_dex))
            except:
                print('attribute update error')

        self.update_totals()

    def constitution_combo_changed(self):
        '''
        if previous selection was a number add it back to all attributes.
        update the current selection and remove from all other attributes if a number
        :return:
        none
        '''
        if self.cur_con != 'Select One':
            self.strength_combo.addItem(self.cur_con)
            self.dexterity_combo.addItem(self.cur_con)
            self.intelligence_combo.addItem(self.cur_con)
            self.wisdom_combo.addItem(self.cur_con)
            self.charisma_combo.addItem(self.cur_con)

        self.cur_con = self.constitution_combo.currentText()

        if self.cur_con != 'Select One':
            try:
                self.strength_combo.removeItem(self.strength_combo.findText(self.cur_con))
                self.dexterity_combo.removeItem(self.dexterity_combo.findText(self.cur_con))
                self.intelligence_combo.removeItem(self.intelligence_combo.findText(self.cur_con))
                self.wisdom_combo.removeItem(self.wisdom_combo.findText(self.cur_con))
                self.charisma_combo.removeItem(self.charisma_combo.findText(self.cur_con))
            except:
                print('attribute update error')

        self.update_totals()

    def intelligence_combo_changed(self):
        '''
        if previous selection was a number add it back to all attributes.
        update the current selection and remove from all other attributes if a number
        :return:
        none
        '''
        if self.cur_int != 'Select One':
            self.strength_combo.addItem(self.cur_int)
            self.dexterity_combo.addItem(self.cur_int)
            self.constitution_combo.addItem(self.cur_int)
            self.wisdom_combo.addItem(self.cur_int)
            self.charisma_combo.addItem(self.cur_int)

        self.cur_int = self.intelligence_combo.currentText()

        if self.cur_int != 'Select One':
            try:
                self.strength_combo.removeItem(self.strength_combo.findText(self.cur_int))
                self.dexterity_combo.removeItem(self.dexterity_combo.findText(self.cur_int))
                self.constitution_combo.removeItem(self.constitution_combo.findText(self.cur_int))
                self.wisdom_combo.removeItem(self.wisdom_combo.findText(self.cur_int))
                self.charisma_combo.removeItem(self.charisma_combo.findText(self.cur_int))
            except:
                print('attribute update error')

        self.update_totals()

    def wisdom_combo_changed(self):
        '''
        if previous selection was a number add it back to all attributes.
        update the current selection and remove from all other attributes if a number
        :return:
        none
        '''
        if self.cur_wis != 'Select One':
            self.strength_combo.addItem(self.cur_wis)
            self.dexterity_combo.addItem(self.cur_wis)
            self.constitution_combo.addItem(self.cur_wis)
            self.intelligence_combo.addItem(self.cur_wis)
            self.charisma_combo.addItem(self.cur_wis)

        self.cur_wis = self.wisdom_combo.currentText()

        if self.cur_wis != 'Select One':
            try:
                self.strength_combo.removeItem(self.strength_combo.findText(self.cur_wis))
                self.dexterity_combo.removeItem(self.dexterity_combo.findText(self.cur_wis))
                self.constitution_combo.removeItem(self.constitution_combo.findText(self.cur_wis))
                self.intelligence_combo.removeItem(self.intelligence_combo.findText(self.cur_wis))
                self.charisma_combo.removeItem(self.charisma_combo.findText(self.cur_wis))
            except:
                print('attribute update error')

        self.update_totals()

    def charisma_combo_changed(self):
        '''
        if previous selection was a number add it back to all attributes.
        update the current selection and remove from all other attributes if a number
        :return:
        none
        '''
        if self.cur_cha != 'Select One':
            self.strength_combo.addItem(self.cur_cha)
            self.dexterity_combo.addItem(self.cur_cha)
            self.constitution_combo.addItem(self.cur_cha)
            self.intelligence_combo.addItem(self.cur_cha)
            self.wisdom_combo.addItem(self.cur_cha)

        self.cur_cha = self.charisma_combo.currentText()

        if self.cur_cha != 'Select One':
            try:
                self.strength_combo.removeItem(self.strength_combo.findText(self.cur_cha))
                self.dexterity_combo.removeItem(self.dexterity_combo.findText(self.cur_cha))
                self.constitution_combo.removeItem(self.constitution_combo.findText(self.cur_cha))
                self.intelligence_combo.removeItem(self.intelligence_combo.findText(self.cur_cha))
                self.wisdom_combo.removeItem(self.wisdom_combo.findText(self.cur_cha))
            except:
                print('attribute update error')

        self.update_totals()

    def update_totals(self):
        '''
        takes all stat inputs and updates the total number
        :return:
        none
        '''
        self.strength_total_LCD.display(
            (int(self.strength_combo.currentText()) if self.strength_combo.currentText().isnumeric() else 0)
            + self.strength_race_spinbox.value() + self.strength_class_spinbox.value() + self.strength_level_spinbox.value())
        self.dexterity_total_LCD.display(
            (int(self.dexterity_combo.currentText()) if self.dexterity_combo.currentText().isnumeric() else 0)
            + self.dexterity_race_spinbox.value() + self.dexterity_class_spinbox.value() + self.dexterity_level_spinbox.value())
        self.constitution_total_LCD.display(
            (int(self.constitution_combo.currentText()) if self.constitution_combo.currentText().isnumeric() else 0)
            + self.constitution_race_spinbox.value() + self.constitution_class_spinbox.value() + self.constitution_level_spinbox.value())
        self.intelligence_total_LCD.display(
            (int(self.intelligence_combo.currentText()) if self.intelligence_combo.currentText().isnumeric() else 0)
            + self.intelligence_race_spinbox.value() + self.intelligence_class_spinbox.value() + self.intelligence_level_spinbox.value())
        self.wisdom_total_LCD.display(
            (int(self.wisdom_combo.currentText()) if self.wisdom_combo.currentText().isnumeric() else 0)
            + self.wisdom_race_spinbox.value() + self.wisdom_class_spinbox.value() + self.wisdom_level_spinbox.value())
        self.charisma_total_LCD.display(
            (int(self.charisma_combo.currentText()) if self.charisma_combo.currentText().isnumeric() else 0)
            + self.charisma_race_spinbox.value() + self.charisma_class_spinbox.value() + self.charisma_level_spinbox.value())

        self.strength_modifier_LCD.display(((self.strength_total_LCD.intValue() - 10) // 2))
        self.dexterity_modifier_LCD.display(((self.dexterity_total_LCD.intValue() - 10) // 2))
        self.constitution_modifier_LCD.display(((self.constitution_total_LCD.intValue() - 10) // 2))
        self.constitution_modifier_hp_LCD.display(self.constitution_modifier_LCD.intValue())
        self.hp_total_LCD.display(
            self.hp_class_spinbox.value() + self.hp_bonus_spinbox.value()
            + self.constitution_modifier_hp_LCD.intValue() + self.hp_level_spinbox.value())
        self.intelligence_modifier_LCD.display(((self.intelligence_total_LCD.intValue() - 10) // 2))
        self.wisdom_modifier_LCD.display(((self.wisdom_total_LCD.intValue() - 10) // 2))
        self.charisma_modifier_LCD.display(((self.charisma_total_LCD.intValue() - 10) // 2))