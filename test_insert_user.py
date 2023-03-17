import unittest
#import the api funtion below
from add_user import insert_user
# after import the test would be initiated
import datetime


class TestInsertUser(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        # Set up variables
        
        self.user_name_too_short = "joe"
        self.user_name_not_string = 2345
        self.user_name_too_long = "johndoe_janedoe"
        self.user_name_is_valid = "joseph"
        
        self.dob_not_date = '2200, 1, 1'
        self.dob_too_young = datetime.date(2200, 1, 1)
        self.dob_future_date = datetime.date(2600, 1, 1)
        self.dob_is_valid = datetime.date(1980, 1, 1)

        self.email_not_string = ['joey@yahoo.com']
        self.email_no_domain ="joe@"
        self.email_no_prefix ="@gmail.com"
        self.email_no_at ="joe_kundabox.com"
        self.email_is_valid = "janedoe@gmail.com"
        
        self.password_not_string = ('Abbc123fjj')
        self.password_is_valid = "&Sdrq9afd93e"
        self.password_less_than_two_numbers ="joe@"
        self.password_no_uppercase ="joe@"
        self.password_no_lowercase ="joe@"
        self.password_too_short ="joe@"
        self.password_too_long = "12Anbjohndoe_435janed&uj1"

        self.user_name_already_inserted = "joe"
        self.dob_is_already_inserted = datetime.date(1900, 1, 1)
        self.email_already_inserted = "joe@kundabox.com"
        self.password_already_inserted = "12ABCabc"
        
        
    @classmethod
    def tearDownClass(self):
        print("tear down")
        """# Clean up the test database after each test
        self.conn.close()"""
        
    def test_user_name_too_long(self):
        "Adding a user with user name that is too short"

        inserted_data = insert_user( self.user_name_too_long, 
                                     self.dob_is_valid, 
                                     self.email_is_valid, 
                                     self.password_is_valid )
        self.assertEqual(inserted_data["result"], False)
        self.assertEqual( inserted_data["code"], "INVALID_NAME")

    def test_user_name_too_short(self):        
        "Adding a user with user name that is too short"

        inserted_data = insert_user( self.user_name_too_short, 
                                     self.dob_is_valid, 
                                     self.email_is_valid, 
                                     self.password_is_valid )
        self.assertEqual(inserted_data["result"], False)
        self.assertEqual( inserted_data["code"], "INVALID_NAME")

    def test_user_name_not_string(self):
        "Adding a user with user name that is not string"
        inserted_data = insert_user( self.user_name_not_string, 
                                     self.dob_is_valid, 
                                     self.email_is_valid, 
                                     self.password_is_valid )
        self.assertEqual(inserted_data["result"], False)
        self.assertEqual( inserted_data["code"], "INVALID_NAME")

    def test_dob_not_date(self):
        "Adding a user with dob that is not date"

        inserted_data = insert_user( self.user_name_is_valid, 
                                     self.dob_not_date, 
                                     self.email_is_valid, 
                                     self.password_is_valid )
        self.assertEqual(inserted_data["result"], False)
        self.assertEqual( inserted_data["code"], "INVALID_DOB")

    def test_dob_too_young(self):
        "Adding a user with age too young"

        inserted_data = insert_user( self.user_name_is_valid, 
                                     self.dob_too_young, 
                                     self.email_is_valid, 
                                     self.password_is_valid )
        self.assertEqual(inserted_data["result"], False)
        self.assertEqual( inserted_data["code"], "INVALID_DOB")

        "Adding a user with future date"
        inserted_data = insert_user( self.user_name_is_valid, 
                                     self.dob_future_date, 
                                     self.email_is_valid, 
                                     self.password_is_valid )
        self.assertEqual(inserted_data["result"], False)
        self.assertEqual( inserted_data["code"], "INVALID_DOB")

    def test_email_not_string(self):
        "Adding a user with email that is not string"

        inserted_data = insert_user( self.user_name_is_valid, 
                                     self.dob_is_valid, 
                                     self.email_not_string, 
                                     self.password_is_valid )
        self.assertEqual(inserted_data["result"], False)
        self.assertEqual( inserted_data["code"], "INVALID_EMAIL")
        
    def test_email_non_valid(self):
        "Adding a user with email that has no domain"

        inserted_data = insert_user( self.user_name_is_valid, 
                                     self.dob_is_valid, 
                                     self.email_no_domain, 
                                     self.password_is_valid )
        self.assertEqual(inserted_data["result"], False)
        self.assertEqual( inserted_data["code"], "INVALID_EMAIL")

        "Adding a user with email that has no prefix"

        inserted_data = insert_user( self.user_name_is_valid, 
                                     self.dob_is_valid, 
                                     self.email_no_prefix, 
                                     self.password_is_valid )
        self.assertEqual(inserted_data["result"], False)
        self.assertEqual( inserted_data["code"], "INVALID_EMAIL")

        "Adding a user with email that has no @"

        inserted_data = insert_user( self.user_name_is_valid, 
                                     self.dob_is_valid, 
                                     self.email_no_at, 
                                     self.password_is_valid )
        self.assertEqual(inserted_data["result"], False)
        self.assertEqual( inserted_data["code"], "INVALID_EMAIL")
    
    def test_password_not_string(self):
        "Adding a user with password that is not string"

        inserted_data = insert_user( self.user_name_is_valid, 
                                     self.dob_is_valid, 
                                     self.email_is_valid, 
                                     self.password_not_string )
        self.assertEqual(inserted_data["result"], False)
        self.assertEqual( inserted_data["code"], "INVALID_PASSWORD")

    def test_password_too_long(self):
        "Adding a user with password that is too long"

        inserted_data = insert_user( self.user_name_is_valid, 
                                     self.dob_is_valid, 
                                     self.email_is_valid, 
                                     self.password_too_long )
        self.assertEqual(inserted_data["result"], False)
        self.assertEqual( inserted_data["code"], "INVALID_PASSWORD")

    def test_password_too_short(self):
        "Adding a user with password that is too short"

        inserted_data = insert_user( self.user_name_is_valid, 
                                     self.dob_is_valid, 
                                     self.email_is_valid, 
                                     self.test_password_too_short )
        self.assertEqual(inserted_data["result"], False)
        self.assertEqual( inserted_data["code"], "INVALID_PASSWORD")

    def test_password_not_valid(self):
        "Adding a user with password that has less than two numbers"

        inserted_data = insert_user( self.user_name_is_valid, 
                                     self.dob_is_valid, 
                                     self.email_is_valid, 
                                     self.password_less_than_two_numbers)
        self.assertEqual(inserted_data["result"], False)
        self.assertEqual( inserted_data["code"], "INVALID_PASSWORD")


        "Adding a user with password that has no lower case"

        inserted_data = insert_user( self.user_name_is_valid, 
                                     self.dob_is_valid, 
                                     self.email_is_valid, 
                                     self.password_no_lowercase)
        self.assertEqual(inserted_data["result"], False)
        self.assertEqual( inserted_data["code"], "INVALID_PASSWORD")

        "Adding a user with password that has no upper case"

        inserted_data = insert_user( self.user_name_is_valid, 
                                     self.dob_is_valid, 
                                     self.email_is_valid, 
                                     self.password_no_uppercase)
        self.assertEqual(inserted_data["result"], False)
        self.assertEqual( inserted_data["code"], "INVALID_PASSWORD")

    def test_user_already_inserted(self):
        "Adding a user already inserted in database"

        inserted_data = insert_user( self.user_name_already_inserted, 
                                     self.dob_is_already_inserted, 
                                     self.email_already_inserted, 
                                     self.password_already_inserted)
        self.assertEqual(inserted_data["result"], False)
        self.assertEqual( inserted_data["code"], "USER_ALREADY_REGISTERED")
        

    def test_add_user_proper_values(self):
        "Adding a user with proper values"

        inserted_data = insert_user( self.user_name_is_valid, 
                                     self.dob_is_valid, 
                                     self.email_is_valid, 
                                     self.password_is_valid)
        self.assertEqual(inserted_data["result"], True)
        

   
if __name__ =="__main__":
    unittest.main()
