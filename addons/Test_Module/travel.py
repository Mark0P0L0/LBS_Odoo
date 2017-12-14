from osv import osv, fields
#copy as much as you need to create all the objects you need, just rename(Ideally, you would copy that bunch of code
# several times to create all the entities you need (travel_airport, travel_room, travel_flight). This is what will
# hold the database structure of your objects, but you don't really need to worry too much about the database side.
# Just filling this file will create the system structure for you when you install the module.).
class travel_hostel(osv.osv):
       _name = 'travel.hostel'
       _inherit = 'res.partner'
       _columns = {
       'rooms_id': fields.one2many('travel.room', 'hostel_id', 'Rooms'),
       'quality': fields.char('Quality', size=16),
       }
       _defaults = {
       }
travel_hostel()
