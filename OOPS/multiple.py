class employee:
    def emp_details(self, id, name):
        self.idno=id
        self.na=name
class org:
    def company(self,org_name):
        self.co_name=org_name
class dip(employee, org):
    def display(self):
        print(self.idno)
        print(self.na)
        print(self.co_name)
d=dip()
d.emp_details(10001, "Vijay")
d.company("abc PVT LTD")
d.display()
