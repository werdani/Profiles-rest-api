# Profiles REST API  

### APIView VS ViewSet :
##### to create our api .
##### APIView : is the most basic type of view, apiview that is allow us to define functions that match the standerd HTTP protocole . 
* Describe logic to make API endpoint .
* Uses standard HTTP methods for functions .
* Calling other APIs .
* working with local files .

### Whene to use APIViews ? 
- Need full control over the logic .
- Processing files and rendering a synhoronous response .
- You are calling other APIa / services .
- Accessign local files or data .

### what are the ViewSets ?
* takes care of a lot of typical logic for you .
* uses midel operations for functins .
* perfect for standard datavase operaions .
* fastest way to make a database interface .

### Whene to use ViewSetes ?
- A simple CRUD interface to your database .
- A quick and simple API .
- Little to no customizaion on the logic .
- Working with standard data structures .