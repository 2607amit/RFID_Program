# -*- coding: utf-8 -*-
"""
Created on Wed Mar  5 19:53:53 2025

@author: Dell
"""

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QComboBox, QLineEdit
import sys

LINE_NAME_MAPPING = {
    "0000": "Up Signal",
    "0001": "Down Signal",
    "0010": "Up Fast Signal",
    "0011": "Down Fast Signal",
    "1000": "Up Slow Signal",
    "1001": "Down Slow Signal",
    "1010": "Up Main Signal",
    "1011": "Down Main Signal",
    "1100": "Up Sub Signal",
    "1101": "Down Sub Signal",
    "1110": "UP BI-Direction",
    "1111": "DN BI-Direction"
}

SIGNAL_TYPE_MAPPING = {
    "010000": "Distant Signal",
    "010001": "Inner Distant Signal",
    "010010": "Gate Distant Signal",
    "010011": "Gate Inner Distant Signal",
    "010100": "IB Distant Signal",
    "010101": "IB Inner Distant Signal",
    "010110": "Auto Signal",
    "010111": "Semi-Automatic Signal with A-marker lit",
    "100100": "Semi Automatic Signal without A marker lit"
}

def binary_to_decimal(binary_str):
    return int(binary_str, 2)

def decimal_to_binary(decimal_value):
    return format(decimal_value, '015b')

def process_inputs(signal_type, line_name, line_number):
    concatenated_binary = signal_type + line_name + line_number
    decimal_value = binary_to_decimal(concatenated_binary)
    return concatenated_binary, decimal_value

def extract_values(decimal_value):
    binary_str = decimal_to_binary(decimal_value)
    signal_type = binary_str[:6]
    line_name = binary_str[6:10]
    line_number = binary_str[10:]
    return binary_str, signal_type, line_name, line_number

class BinaryConverterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Binary to Decimal Converter")
        self.setGeometry(100, 100, 400, 350)

        self.layout = QVBoxLayout()

        self.label1 = QLabel("Select Signal Type:")
        self.signal_type_dropdown = QComboBox()
        self.signal_type_input = QLineEdit()
        for key, value in SIGNAL_TYPE_MAPPING.items():
            self.signal_type_dropdown.addItem(value, key)
        self.signal_type_dropdown.currentIndexChanged.connect(self.update_signal_type_input)
        self.layout.addWidget(self.label1)
        self.layout.addWidget(self.signal_type_dropdown)
        self.layout.addWidget(self.signal_type_input)

        self.label2 = QLabel("Select Line Name:")
        self.line_name_dropdown = QComboBox()
        self.line_name_input = QLineEdit()
        for key, value in LINE_NAME_MAPPING.items():
            self.line_name_dropdown.addItem(value, key)
        self.line_name_dropdown.currentIndexChanged.connect(self.update_line_name_input)
        self.layout.addWidget(self.label2)
        self.layout.addWidget(self.line_name_dropdown)
        self.layout.addWidget(self.line_name_input)

        self.label3 = QLabel("Enter Line Number (Binary String):")
        self.input3 = QLineEdit()
        self.layout.addWidget(self.label3)
        self.layout.addWidget(self.input3)

        self.button = QPushButton("Submit")
        self.button.clicked.connect(self.on_submit)
        self.layout.addWidget(self.button)

        self.result_label = QLabel("")
        self.layout.addWidget(self.result_label)

        self.setLayout(self.layout)

    def update_signal_type_input(self):
        self.signal_type_input.setText(self.signal_type_dropdown.currentData())

    def update_line_name_input(self):
        self.line_name_input.setText(self.line_name_dropdown.currentData())

    def on_submit(self):
        signal_type = self.signal_type_input.text()
        line_name = self.line_name_input.text()
        line_number = self.input3.text()

        concatenated_binary, decimal_value = process_inputs(signal_type, line_name, line_number)
        binary_str, signal_type_ex, line_name_ex, line_number_ex = extract_values(decimal_value)

        result_text = (f"Concatenated Binary: {concatenated_binary}\n"
                       f"Decimal Value: {decimal_value}\n"
                       f"Binary Representation: {binary_str}\n"
                       f"Signal Type: {SIGNAL_TYPE_MAPPING.get(signal_type_ex, 'Unknown')}\n"
                       f"Line Name: {LINE_NAME_MAPPING.get(line_name_ex, 'Unknown')}\n"
                       f"Line Number: {line_number_ex}")
        self.result_label.setText(result_text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BinaryConverterApp()
    window.show()
    sys.exit(app.exec_())
