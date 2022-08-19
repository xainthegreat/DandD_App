# ###################save this##################
#
# newCharacterForm.self.label_result = newCharacterForm.self.findChild(QLabel, "testLabel")
#
# newCharacterForm.self.combo = newCharacterForm.self.findChild(QComboBox, "raceComboBox")
#
# # connected combobox signal
# newCharacterForm.self.combo.currentTextChanged.connect(newCharacterForm.self.combo_changed)
#
#
# def combo_changed(self):
#     item = self.combo.currentText()
#     self.label_result.setText("Your Account Type Is : " + item)
#
# ################save this#################
#
#     def class_combo_changed(self):
#         current_class_selection = CLASSES[self.class_combo.currentText().lower()]
#         print(current_class_selection)
#         self.hp_class_start.display(current_class_selection['hit_die'])
#         self.starting_equipment.clear()
#         # self.starting_equipment.addItems(current_class_selection["starting_equipment"]) #todo this is borked
#
