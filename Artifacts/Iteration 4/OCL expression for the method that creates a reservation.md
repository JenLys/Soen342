**Note: this ocl is not based on the most recent code since the latter got modified to interact with the sql tables fully. It is based on the code present before the full persistence implementation

Context
BookingDB::create_reservation(fname: String,lname: String,age:int,selected_option: String, user_id: String, current: boolean)

<ins> pre </ins> <br>
--the passed used exists <br>
self.User ---> exists(User.user_id = user_id) <br>
--the option selected is valid (it exists (existing id passed) and is not void) <br>
self.result_id <> null and <br>
self.Console.Journey ---> exists(j: Journey| j.result_id = selected_option) <br>

<ins> post </ins> <br>

--reservation created under the user's name <br>
self.Reservation ---> exists(r:Reservation | r.fname = fname and r.lname = lname) <br>
--trip object created + contains reservation <br>
self.Trip ---> exists(t: Trip | t.user_id = user_id and t.Reservation ---> exists(self.selected_option = selected_option)) <br>
--update size of trip since it contains the reservation <br>
self.trip ---> size() = self.trip@pre <br>
          ---> size() + 1 <br>
--ticket created for the user <br>
self.Ticket ---> exists(tk: Ticket | tk.user_id = user_id) <br>
