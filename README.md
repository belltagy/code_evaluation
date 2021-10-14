# code_evaluation
code evaluation for  integrity lab
## setup project ""
1. excute the following on your shell to runserver 
      ``` >>> pipenv install 
          >>> pipenv shell
          >>> python manage.py migrate
          >>> python manage.py runserver
 2. got the folowing url to excute apis queries
    '''
       http://127.0.0.1:8000/api/authors-list/?query=(name startswith A)
  
  3. the main code that parse string to Q query located in books/service.py
  4. to check where  parse_search_phrase is called go to books/api/views.py 
          
