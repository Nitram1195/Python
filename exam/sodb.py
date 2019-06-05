#!/usr/bin/env python3


import json
import sys


class Databaze():
    def __init__(self):
        self._objekty = []
        self.inicializuj()


    def inicializuj(self):
        with open ("default.sodb") as f:
            for line in f:
                line_data = json.loads(line)
                self._objekty.append(line_data)


    def insert(self, objekt):
        try:
            id_noveho = objekt["id"]
            if self.check_object(objekt):
                print(f"An entry with id {id_noveho} is already contained in the DB")
            else:
                while(self.check_id(id_noveho)==False):
                    id_noveho +=  1
                objekt["id"] = id_noveho
                with open ("default.sodb", "a") as f:
                    f.write(str(objekt).replace("\'","\"")+"\n")
                print(f"Entry succesfully inserted with id {id_noveho}")

        except KeyError:
            id_noveho = 1
            if self.check_object(objekt):
                print(f"An entry with id {id_noveho} is already contained in the DB")
            else:
                while(self.check_id(id_noveho)==False):
                    id_noveho +=  1
                objekt["id"] = id_noveho
                with open ("default.sodb", "a") as f:
                    f.write(str(objekt).replace("\'","\"")+"\n")
                print(f"Entry succesfully inserted with id {id_noveho}")

    
    def delete(self):
        print(f"{len(self._objekty)} entries deleted") 
        with open ("default.sodb", "w") as f:
            del(self._objekty[:])
            f.write("")

    def select(self):
        if self._objekty:
            for objekt in self._objekty:
                print(str(objekt).replace("\'","\""))
            print(f"Total: {len(self._objekty)} entries")
        else:
            print("No entries found in DB")


    def check_id(self, id_noveho):
        for objekt in self._objekty:
            if objekt["id"] == id_noveho:
                return False
        return True


    def check_object(self, objekt):
        for o in self._objekty:
            if o == objekt:
                return True
        return False 

class ObjektDatabaze():
    def __init__(self,idd):
        self._id = idd

if __name__ == "__main__":
    moje_databaze = Databaze()
    if sys.argv[1] == "insert":
        try:
            data = json.loads(sys.argv[2])
            moje_databaze.insert(data)
        except:
            print("Invalid specification of an entry")
    elif sys.argv[1] == "select":
        moje_databaze.select()
    elif sys.argv[1] == "delete":
        moje_databaze.delete()
