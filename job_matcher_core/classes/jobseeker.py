from job_matcher_core.common.const import data_folder_path

class JobSeeker():

    # This class is used to represent a Job Seeker.

    csv_path = f'{data_folder_path}/jobseekers.csv'

    def __init__(self, input, row_no):
        try:
            self.row_no = row_no

            input_fields = self.validate_input(input, row_no)

            self.id = self.get_id(input_fields[0], row_no)
            self.name = self.get_name(input_fields[1], row_no)
            self.skills = self.get_skills(input_fields[2], row_no)

        except Exception as e:
            raise Exception(e)


    def validate_input(self, input, row_no):

        if len(input) != 3:
            raise Exception(f'ERROR: Wrong number of fields in row={row_no} of jobseekers.csv')
        
        return input


    def get_id(self, input, row_no):

        if not input.isdigit():
            raise Exception(f'ERROR: Id field is not an integer in row={row_no} of jobseekers.csv')
        
        return int(input)
    

    def get_name(self, input, row_no):

        # TODO
        # Perform any validation here
        
        return input
    

    def get_skills(self, input, row_no):
    
        # TODO
        # Ideally we should be checking that each of these returned list items is a valid skill string

        return set([field.strip() for field in input.split(',')])


    def __repr__(self):

        # To print: 
        #   print(repr(jobseeker))
        
        return f'id : {self.id},\n\
        name : {self.name},\n\
        skills : {self.skills}'
