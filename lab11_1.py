import MessageBox


class Course:

    cid = ""
    school = ""
    state = ""
    title = ""
    unit = 0

    def __init__(self):
        self.state = "California"

    def getcost(self):
        return self.unit * 19.5

c1 = Course()
c1.cid = "CIS247"
c1.school = "Cicada College"
c1.title = "Python Programming"
c1.unit = 3
c2 = Course()
c2.cid = "CIS246"
c2.school = "Fred University"
c2.title = "PHP Programming"
c2.unit = 3
c3 = Course()
c3.cid = "CIS245"
c3.school = "Betrice University"
c3.title = "Perl Programming"
c3.unit = 3

s = "CourseID\tCourse Title\tCredit\tSchool\tTotal\n"
s += c1.cid + "\t" + c1.title + "\t" + str(c1.unit) + "\t" + c1.school + "\t" + str(c1.getcost()) + "\n"
s += c2.cid + "\t" + c2.title + "\t" + str(c2.unit) + "\t" + c2.school + "\t" + str(c2.getcost()) + "\n"
s += c3.cid + "\t" + c3.title + "\t" + str(c3.unit) + "\t" + c3.school + "\t" + str(c3.getcost()) + "\n"

MessageBox.Show(s)

