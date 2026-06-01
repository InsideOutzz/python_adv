from abc import ABC,abstractmethod
from streamlit import streamlit as st

class Person(ABC):
    def __init__(self,name,age,weight,height):
        self.name = name
        self.age = age
        self._weight = weight
        self._height = height

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self,value):
        if value < 0:
            raise ValueError("Weight must be positive")
        self._weight = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value < 0:
            raise ValueError("height must be positive")
        self._height = value



    @abstractmethod
    def calculate_bmi(self):
            pass

    @abstractmethod
    def get_bmi_category(self):
            pass


    def print_info(self):
            print(f"Name: {self.name}, Age: {self.age}, Weight: {self.weight}, Height: {self.height} m,"
                  f"Bmi: {self.calculate_bmi():.2f}, Category: {self.get_bmi_category()}")

class Adult(Person):
    def calculate_bmi(self):
                return self._weight * self._height / 100

    def get_bmi_category(self):

        bmi = self.calculate_bmi()

        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 25:
            return "Normal weight"
        elif 25 <= bmi < 30:
            return "Overweight"

        else:
            return "Obese"

class Child(Person):
        def calculate_bmi(self):
            return self._weight * self._height / 100

        def get_bmi_category(self):
            bmi = self.calculate_bmi()

            if bmi < 14:
                return "Underweight"
            elif 14 <= bmi < 18:
                return "Normal weight"
            elif 18 <= bmi < 24:
                return "Overweight"
            else:
                return "Obese"
class BMIapp:
        def __init__(self):
            self.people = []


        def add_person(self,person):
            self.people.append(person)

        def collect_user_data(self):

            name = st.text_input("Enter your name: ")
            age = st.number_input(input("Enter your age: "))
            height = st.number_input(input("Enter your height: "))
            weight = st.number_input(input("Enter your weight: "))

            if st.button("Add Person"):
                if age >= 18:
                  person = Adult(name,age,weight,height)
                else:
                  person = Child(name,age,weight,height)

                self.add_person(person)
                st.success(f"{name} has been added to your group.")

        def print_result(self):

            st.subheader("Result")
            for person in self.people:
                st.write(person.print_info())

        def run(self):


                self.collect_user_data()
                if self.people:
                   self.print_result()

if __name__ == '__main__':
     app = BMIapp()
     app.run()
