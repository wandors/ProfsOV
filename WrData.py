# -*- coding: utf-8 -*-
import os
import tempfile
import pickle


class Datas:
    pathtemp = tempfile.gettempdir() + "/Proftemp"
    def params(self, soname="", name="", father="", birsdey="", profov="", stt="", begin_dey="", DSR="", ZBM="", UDZ="", end_dey="", PHOT="", VID="", OUTS=""):
        self.soname = soname
        self.name = name
        self.father = father
        self.birsdey = birsdey
        self.profov = profov
        self.stt = stt
        self.begin_dey = begin_dey
        self.DSR = DSR
        self.ZBM = ZBM
        self.UDZ = UDZ
        self.photo = PHOT
        self.vid = VID
        self.end_dey = end_dey
        self.outs = OUTS
        self.vid = VID
        self.photo = PHOT

    def wridata(self, filer):
        try:
            self.op = open(filer, "rb")
            self.data = pickle.load(self.op)
            self.op.close()
            self.lostd = self.soname + " " + self.name + " " + self.father
            self.prifis = {"soname": self.soname, "name": self.name, "father": self.father,
                           "birsdey": self.birsdey, "profov": self.profov, "stt": self.stt,
                           "begin_dey": self.begin_dey, "DSR": self.DSR, "ZBM": self.ZBM,
                           "UDZ": self.UDZ, "end_dey": self.end_dey, "VID": self.vid,
                           "PHOT": self.photo, "OUTS": self.outs}
            try:
                self.prw = self.data[self.profov]
                self.prw[self.lostd] = self.prifis
            except:
                self.data[self.profov] = {self.lostd: self.prifis}
            self.dbfile = open(filer, 'wb')
            self.dbms = self.data
            pickle.dump(self.dbms, self.dbfile)
            self.dbfile.close()
        except:
            self.lostd = self.soname + " " + self.name + " " + self.father
            self.prifis = {"soname": self.soname, "name": self.name, "father": self.father,
                           "birsdey": self.birsdey, "profov": self.profov, "stt": self.stt,
                           "begin_dey": self.begin_dey, "DSR": self.DSR, "ZBM": self.ZBM,
                           "UDZ": self.UDZ, "end_dey": self.end_dey, "VID": self.vid, "PHOT": self.phot, "OUTS": self.outs}
            self.proflist = {self.profov: {self.lostd: self.prifis}}
            self.dbfile = open(filer, 'wb')
            self.dbms = self.proflist
            pickle.dump(self.dbms, self.dbfile)
            self.dbfile.close()

    def __savss(self):
        self.datid = self.prolist
        self.dbfile = open(filer, 'wb')
        self.dbms = self.datid
        pickle.dump(self.dbms, self.dbfile)
        self.dbfile.close()

    def reddata(self, files):
            self.files = files
            self.opfil = open(self.files, "rb")
            self.data = pickle.load(self.opfil)
            self.opfil.close()
            return self.data

    def Editers(self, _soname, _name, _father, _birsdey, _profov, _stt, _begin_dey, _DSR, _ZBM, _UDZ, _end_dey, _VID, _PHOT, _OUTS):
        self.__soname = _soname
        self.__name = _name
        self.__father = _father
        self.__brsd = _birsdey
        self.__profer = _profov
        self.__sttu = _stt
        self.__begistr = _begin_dey
        self.__dsr = _DSR
        self.__zbm = _ZBM
        self.__udz = _UDZ
        self.__endstr = _end_dey
        self.__vid = _VID
        self.__PHOT = _PHOT
        self.__OUTS = _OUTS
        self.namepro = [self.__soname, self.__name, self.__father, self.__brsd, self.__profer, self.__sttu,
                        self.__begistr, self.__dsr, self.__zbm, self.__udz, self.__endstr, self.__vid, self.__PHOT, self.__OUTS]
        self.dbfile = open(self.pathtemp + "/Prof.dbsl", 'wb')
        self.dbms = self.namepro
        pickle.dump(self.dbms, self.dbfile)
        self.dbfile.close()

    def Deleter(self, _prf):
        self.filess = self.pathtemp + "/Profs.dbsp"
        with open(self.filess, "r") as f:
            self.filest = f.read()
            f.close()
        self.op = open(self.filest, "rb")
        self.data = pickle.load(self.op)
        self.op.close()
        self.Fulname = "{0} {1} {2}".format(_prf[0], _prf[1], _prf[2])
        self.data[_prf[4]].pop(self.Fulname)
        self.dbfile = open(self.filest, 'wb')
        self.dbms = self.data
        pickle.dump(self.dbms, self.dbfile)
        self.dbfile.close()
