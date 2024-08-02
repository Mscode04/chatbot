from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('jarvis', logic_adapters=['chatterbot.logic.BestMatch',

{'import_path': 'chatterbot.logic.BestMatch', 
'default_response': 'I am sorry, but I do not understand.',
'maximum similarity_threshold': 0.90}])

def chatbotfun(qstn):

    trainer = ListTrainer(bot)

    trainer.train([

    "What are the Institution details",
    "Govt.Polytechnic College,Manjappetty,Nedumkandam, Idukki,685553",

    "details of institution",
    "Govt.Polytechnic College,Manjappetty,Nedumkandam, Idukki,685553",

    "college details(name,address)",
    "Govt.Polytechnic College,Manjappetty,Nedumkandam, Idukki,685553",

    "What is the Address of institution",
    "Govt.Polytechnic College,Manjappetty,Nedumkandam, Idukki,685553",

    "address details of college",
    "Govt.Polytechnic College,Manjappetty,Nedumkandam, Idukki,685553",
    
    "address",
    "Govt.Polytechnic College,Manjappetty,Nedumkandam, Idukki,685553",

    "location",
    "kerala,nedumkandam,idukki"

    "What is the Name of institution",
    "Govt.Polytechnic College",

    "Name of institution",
    "Govt.Polytechnic College",
    
    "Name of college",
    "Govt.Polytechnic College",

    "Can you tell me the name of the institution",
    "Government polytechnic college.",

    'what is the name of the institution',
    "Government polytechnic college.",

    "Please provide me with the address.",
    "Govt.Polytechnic College, Nedumkandam,idukki",

    "what about the district and city?",
    "kerala,nedumkandam",

    "district and city?",
    "kerala,nedumkandam",

    "Could you please explain about the college",
    """Government Polytechnic College, Nedumkandam is one,
    among the leading technical institutions in highrange since its venture in 1999
    Within a short span of time since its emergence GPTC has become successful in
    establishing itself as a leading premier professional educational institution by
    providing its excellence in the field of technology. It is a matter of immense pride
    that students who crossed the threshold of this pioneer institute are now placed in
    responsible and highly coveted positions all over the world and are contributing
    substantially in various fields""",

    "how is college",
    """Government Polytechnic College, Nedumkandam is one,
    among the leading technical institutions in highrange since its venture in 1999
    Within a short span of time since its emergence GPTC has become successful in
    establishing itself as a leading premier professional educational institution by
    providing its excellence in the field of technology. It is a matter of immense pride
    that students who crossed the threshold of this pioneer institute are now placed in
    responsible and highly coveted positions all over the world and are contributing
    substantially in various fields""",

    "What courses and activities are available",
    "Computer engineering,Computer hardware engineering,Electronics engineering",
    
    "What are the Course categories",
    "Computer engineering,Computer hardware engineering,Electronics engineering",
    
    "Whow many course in there",
    "Computer engineering,Computer hardware engineering,Electronics engineering",
    
    "which are the courses in there",
    "Computer engineering,Computer hardware engineering,Electronics engineering",
    
    "courses",
    "Computer engineering,Computer hardware engineering,Electronics engineering",
    
    "departments",
    "Computer engineering,Computer hardware engineering,Electronics engineering",

    "What is the sanctioned strength",
    "60 on each course",

    "how many seats in one course",
    "60 on each course",

    "what is the max. vacancy",
    "60 on each course",

    "how many vacancy in each department",
    "60 on each course",

    "what is the total strength",
    "60 on each course",

    "Please let me know about the class times",
    "09:30 AM to 03:50 PM",

    "class timing",
    "09:30 AM to 03:50 PM",

    "how long is the classes",
    "09:30 AM to 03:50 PM",

    "at what time classes will start",
    "09:30AM"

    "at what time classes will end",
    "03:50PM"

    "let me know about office timings",
    "09:00 AM to 05:00 PM",
    
    "office timing",
    "09:00 AM to 05:00 PM",
    
    "what is office timing",
    "09:00 AM to 05:00 PM",
    
    "how is office timing",
    "09:00 AM to 05:00 PM",
    
    "how is office timing",
    "09:00 AM to 05:00 PM",

    "when will office close",
    "05:00PM",

    "How about the holidays",
    "all saturday & Govt holidays",

    "holidays",
    "all saturday & Govt holidays",

    "is saturday holiday",
    "yes",

    "Please provide me with your contact information",
    "GPTC Nedumkandam,idukki,kerala,685553 ,Phone : 04868 - 234082 ,gptcnedumkandam@yahoo.co.in, info@gptcnedumkandam.ac.in",

    "contact",
    "GPTC Nedumkandam,idukki,kerala,685553 ,Phone : 04868 - 234082 ,gptcnedumkandam@yahoo.co.in, info@gptcnedumkandam.ac.in",

    "contact details",
    "GPTC Nedumkandam,idukki,kerala,685553 ,Phone : 04868 - 234082 ,gptcnedumkandam@yahoo.co.in, info@gptcnedumkandam.ac.in",

    "how can I contact",
    "GPTC Nedumkandam,idukki,kerala,685553 ,Phone : 04868 - 234082 ,gptcnedumkandam@yahoo.co.in, info@gptcnedumkandam.ac.in",
    

    "What facilities are available there in the institution",
    """Library : Thiru Mahatma Gandhi said, the present day university is
    nothing but a cluster of books. Our library is working as an example for
    the above saying.
    Our Polytechnic College Library possesses many books in an ordered
    manner of various disciplines. It is computerized for the benefit of the
    students and is working 12 hours per day. Books are arranged with the
    retrieve time of less than 1 minute.
    We are providing book bank facilities to the students, thereby; students
    from low financial background can take text books for all their subjects
    with the due period of one semester. In accordance with the objective of
    the College, the library aims to develop a comprehensive collection of
    documents useful for researchers, the faculty and the student community.\n

    ○ Health club : A Healthy mind in a Healthy body so goes the adage.
    The Health Club is home to an ultra modern gymnasium in appropreate
    area, to the needs of the fitness enthusiasts. The staff and students are free
    to use the gymnasium, after class hours under the tutelage of professional
    trainers. The state-of-the-art equipments available include bench press,
    peck deck, bicep curl, lateral pulley and body twister machines.\n

    ○ Hostel : We provide excellent hostel facility for girls is taken care of by
    dedicated concerned staff. Affectionate discipline, tasty food at moderate
    rates and neat rooms with modern sanitation and professional laundry
    services are provided.Hostel Mess based on the dividing system and rent
    as per government norm(Rs.105 per month).\n

    ○ Canteen : We have canteen facility for accession to the students for their
    welfare at all time through out the year.It can accommodate more than
    50 students at a time. It caters the needs of the students of various
    backgrounds. We ensure the foods in neat and affordable rate. Foods
    provided are delicious, tasty and digestive. A month-end-payment facility
    is provided if need.\n

    ○ Auditorium : Our Polytechnic have auditorium which is situated in
    college campus. It is fully electrically furnished with sound system.
    Students cultural activities and PTA association meetings are held on here.

    ○ Transport : The college has a fleet of new bus to cater the transportation
    needs of students and staffs. It is servicing from Nedumkandam to and
    from college. The transportation wing always aims for safety of the
    students and staffs and hence experienced driver is employed to do this
    service.The facility is monthly or daily.""",

    "facilities",
     """Library : Thiru Mahatma Gandhi said, the present day university is
    nothing but a cluster of books. Our library is working as an example for
    the above saying.
    Our Polytechnic College Library possesses many books in an ordered
    manner of various disciplines. It is computerized for the benefit of the
    students and is working 12 hours per day. Books are arranged with the
    retrieve time of less than 1 minute.
    We are providing book bank facilities to the students, thereby; students
    from low financial background can take text books for all their subjects
    with the due period of one semester. In accordance with the objective of
    the College, the library aims to develop a comprehensive collection of
    documents useful for researchers, the faculty and the student community.\n

    ○ Health club : A Healthy mind in a Healthy body so goes the adage.
    The Health Club is home to an ultra modern gymnasium in appropreate
    area, to the needs of the fitness enthusiasts. The staff and students are free
    to use the gymnasium, after class hours under the tutelage of professional
    trainers. The state-of-the-art equipments available include bench press,
    peck deck, bicep curl, lateral pulley and body twister machines.\n

    ○ Hostel : We provide excellent hostel facility for girls is taken care of by
    dedicated concerned staff. Affectionate discipline, tasty food at moderate
    rates and neat rooms with modern sanitation and professional laundry
    services are provided.Hostel Mess based on the dividing system and rent
    as per government norm(Rs.105 per month).\n

    ○ Canteen : We have canteen facility for accession to the students for their
    welfare at all time through out the year.It can accommodate more than
    50 students at a time. It caters the needs of the students of various
    backgrounds. We ensure the foods in neat and affordable rate. Foods
    provided are delicious, tasty and digestive. A month-end-payment facility
    is provided if need.\n

    ○ Auditorium : Our Polytechnic have auditorium which is situated in
    college campus. It is fully electrically furnished with sound system.
    Students cultural activities and PTA association meetings are held on here.

    ○ Transport : The college has a fleet of new bus to cater the transportation
    needs of students and staffs. It is servicing from Nedumkandam to and
    from college. The transportation wing always aims for safety of the
    students and staffs and hence experienced driver is employed to do this
    service.The facility is monthly or daily.""",

    "facilities of college",
     """Library : Thiru Mahatma Gandhi said, the present day university is
    nothing but a cluster of books. Our library is working as an example for
    the above saying.
    Our Polytechnic College Library possesses many books in an ordered
    manner of various disciplines. It is computerized for the benefit of the
    students and is working 12 hours per day. Books are arranged with the
    retrieve time of less than 1 minute.
    We are providing book bank facilities to the students, thereby; students
    from low financial background can take text books for all their subjects
    with the due period of one semester. In accordance with the objective of
    the College, the library aims to develop a comprehensive collection of
    documents useful for researchers, the faculty and the student community.\n

    ○ Health club : A Healthy mind in a Healthy body so goes the adage.
    The Health Club is home to an ultra modern gymnasium in appropreate
    area, to the needs of the fitness enthusiasts. The staff and students are free
    to use the gymnasium, after class hours under the tutelage of professional
    trainers. The state-of-the-art equipments available include bench press,
    peck deck, bicep curl, lateral pulley and body twister machines.\n

    ○ Hostel : We provide excellent hostel facility for girls is taken care of by
    dedicated concerned staff. Affectionate discipline, tasty food at moderate
    rates and neat rooms with modern sanitation and professional laundry
    services are provided.Hostel Mess based on the dividing system and rent
    as per government norm(Rs.105 per month).\n

    ○ Canteen : We have canteen facility for accession to the students for their
    welfare at all time through out the year.It can accommodate more than
    50 students at a time. It caters the needs of the students of various
    backgrounds. We ensure the foods in neat and affordable rate. Foods
    provided are delicious, tasty and digestive. A month-end-payment facility
    is provided if need.\n

    ○ Auditorium : Our Polytechnic have auditorium which is situated in
    college campus. It is fully electrically furnished with sound system.
    Students cultural activities and PTA association meetings are held on here.

    ○ Transport : The college has a fleet of new bus to cater the transportation
    needs of students and staffs. It is servicing from Nedumkandam to and
    from college. The transportation wing always aims for safety of the
    students and staffs and hence experienced driver is employed to do this
    service.The facility is monthly or daily.""",

    "facilities of institution",
     """Library : Thiru Mahatma Gandhi said, the present day university is
    nothing but a cluster of books. Our library is working as an example for
    the above saying.
    Our Polytechnic College Library possesses many books in an ordered
    manner of various disciplines. It is computerized for the benefit of the
    students and is working 12 hours per day. Books are arranged with the
    retrieve time of less than 1 minute.
    We are providing book bank facilities to the students, thereby; students
    from low financial background can take text books for all their subjects
    with the due period of one semester. In accordance with the objective of
    the College, the library aims to develop a comprehensive collection of
    documents useful for researchers, the faculty and the student community.\n

    ○ Health club : A Healthy mind in a Healthy body so goes the adage.
    The Health Club is home to an ultra modern gymnasium in appropreate
    area, to the needs of the fitness enthusiasts. The staff and students are free
    to use the gymnasium, after class hours under the tutelage of professional
    trainers. The state-of-the-art equipments available include bench press,
    peck deck, bicep curl, lateral pulley and body twister machines.\n

    ○ Hostel : We provide excellent hostel facility for girls is taken care of by
    dedicated concerned staff. Affectionate discipline, tasty food at moderate
    rates and neat rooms with modern sanitation and professional laundry
    services are provided.Hostel Mess based on the dividing system and rent
    as per government norm(Rs.105 per month).\n

    ○ Canteen : We have canteen facility for accession to the students for their
    welfare at all time through out the year.It can accommodate more than
    50 students at a time. It caters the needs of the students of various
    backgrounds. We ensure the foods in neat and affordable rate. Foods
    provided are delicious, tasty and digestive. A month-end-payment facility
    is provided if need.\n

    ○ Auditorium : Our Polytechnic have auditorium which is situated in
    college campus. It is fully electrically furnished with sound system.
    Students cultural activities and PTA association meetings are held on here.

    ○ Transport : The college has a fleet of new bus to cater the transportation
    needs of students and staffs. It is servicing from Nedumkandam to and
    from college. The transportation wing always aims for safety of the
    students and staffs and hence experienced driver is employed to do this
    service.The facility is monthly or daily.""",

    "library",
        """Thiru Mahatma
    Gandhi said, the present day university is nothing but a cluster of
    books. Our library is working as an example for the above saying.
    Our Polytechnic College Library possesses many books in an ordered
    manner of various disciplines. It is computerized for the benefit of the
    students and is working 12 hours per day. Books are arranged with the
    retrieve time of less than 1 minute.
    We are providing book bank facilities to the students, thereby; students
    from low financial background can take text books for all their subjects
    with the due period of one semester. In accordance with the objective of
    the College, the library aims to develop a comprehensive collection of
    documents useful for researchers, the faculty and the student community.""",

    "health club",
    """A Healthy mind in a Healthy body’ – so goes the adage. The Health Club
    is home to an ultra modern gymnasium in appropreate area, to the needs of
    the fitness enthusiasts. The staff and students are free to use the
    gymnasium, after class hours under the tutelage of professional trainers.
    The state-of-the-art equipments available include bench press, peck deck,
    bicep curl, lateral pulley and body twister machines""",

    "gym",
    """A Healthy mind in a Healthy body’ – so goes the adage. The Health Club
    is home to an ultra modern gymnasium in appropreate area, to the needs of
    the fitness enthusiasts. The staff and students are free to use the
    gymnasium, after class hours under the tutelage of professional trainers.
    The state-of-the-art equipments available include bench press, peck deck,
    bicep curl, lateral pulley and body twister machines""",

    "hostel",
    """We provide excellent hostel facility for
    girls is taken care of by dedicated concerned staff. Affectionate discipline,
    tasty food at moderate rates and neat rooms with modern sanitation and
    professional laundry services are provided.Hostel Mess based on the
    dividing system and rent as per government norm(Rs.105 per month)""",

    "hostel for boys",
    """We provide excellent hostel facility for
    girls is taken care of by dedicated concerned staff. Affectionate discipline,
    tasty food at moderate rates and neat rooms with modern sanitation and
    professional laundry services are provided.Hostel Mess based on the
    dividing system and rent as per government norm(Rs.105 per month)""",

    "hostel for girls",
    """We provide excellent hostel facility for
    girls is taken care of by dedicated concerned staff. Affectionate discipline,
    tasty food at moderate rates and neat rooms with modern sanitation and
    professional laundry services are provided.Hostel Mess based on the
    dividing system and rent as per government norm(Rs.105 per month)""",
    
    "is there hostel facility",
    """We provide excellent hostel facility for
    girls is taken care of by dedicated concerned staff. Affectionate discipline,
    tasty food at moderate rates and neat rooms with modern sanitation and
    professional laundry services are provided.Hostel Mess based on the
    dividing system and rent as per government norm(Rs.105 per month)""",

    "canteen",
    """We have canteen
    facility for accession to the students for their welfare at all time through
    out the year.It can accommodate more than 50 students at a time. It
    caters the needs of the students of various backgrounds. We ensure the
    foods in neat and affordable rate. Foods provided are delicious, tasty and
    digestive. A month-end-payment facility is provided if need""",

    "canteen facility",
    """We have canteen
    facility for accession to the students for their welfare at all time through
    out the year.It can accommodate more than 50 students at a time. It
    caters the needs of the students of various backgrounds. We ensure the
    foods in neat and affordable rate. Foods provided are delicious, tasty and
    digestive. A month-end-payment facility is provided if need""",

    "is there canteen",
    """We have canteen
    facility for accession to the students for their welfare at all time through
    out the year.It can accommodate more than 50 students at a time. It
    caters the needs of the students of various backgrounds. We ensure the
    foods in neat and affordable rate. Foods provided are delicious, tasty and
    digestive. A month-end-payment facility is provided if need""",

    "auditorium",
    """Our Polytechnic have auditorium
    which is situated in college campus. It is fully electrically furnished with
    sound system. Students cultural activities and PTA association meetings
    are held on here.
    """,

    "hall",
    """Our Polytechnic have auditorium
    which is situated in college campus. It is fully electrically furnished with
    sound system. Students cultural activities and PTA association meetings
    are held on here.
    """,

    "program hall",
    """Our Polytechnic have auditorium
    which is situated in college campus. It is fully electrically furnished with
    sound system. Students cultural activities and PTA association meetings
    are held on here.
    """,

    "is there auditorium/hall",
    """Our Polytechnic have auditorium
    which is situated in college campus. It is fully electrically furnished with
    sound system. Students cultural activities and PTA association meetings
    are held on here.
    """,

    "is there hall to conduct program",
    """Our Polytechnic have auditorium
    which is situated in college campus. It is fully electrically furnished with
    sound system. Students cultural activities and PTA association meetings
    are held on here.
    """,
    
    "bus facility",
    """The college has a fleet of new bus to cater
    the transportation needs of students and staffs. It is servicing from
    Nedumkandam to and from college. The transportation wing always aims
    for safety of the students and staffs and hence experienced driver is
    employed to do this service.The facility is monthly or daily""",

    "transportation",
    """The college has a fleet of new bus to cater
    the transportation needs of students and staffs. It is servicing from
    Nedumkandam to and from college. The transportation wing always aims
    for safety of the students and staffs and hence experienced driver is
    employed to do this service.The facility is monthly or daily""",

    "transportation facilities",
    """The college has a fleet of new bus to cater
    the transportation needs of students and staffs. It is servicing from
    Nedumkandam to and from college. The transportation wing always aims
    for safety of the students and staffs and hence experienced driver is
    employed to do this service.The facility is monthly or daily""",

    "is there bus facilities",  
    """The college has a fleet of new bus to cater
    the transportation needs of students and staffs. It is servicing from
    Nedumkandam to and from college. The transportation wing always aims
    for safety of the students and staffs and hence experienced driver is
    employed to do this service.The facility is monthly or daily""",  

    "which is the affiliated university",
    "state board of technical education,kerala",

    "university",
    "state board of technical education,kerala",


    "What type of institution is this",
    "government",

    "What type of institution",
    "government",

    "type of institution",
    "government",

    "is this an aided institution",
    "government",

    "how to apply for admission",
    """The authorities will
    commence the Kerala polytechnic online application process on the official
    website. Candidates have to visit the official website and complete the
    Kerala polytechnic registration process. They have to enter various details
    in the application form for Kerala polytechnic""",

    "how to apply",
        """The authorities will
    commence the Kerala polytechnic online application process on the official
    website. Candidates have to visit the official website and complete the
    Kerala polytechnic registration process. They have to enter various details
    in the application form for Kerala polytechnic""",


    "how to get admission",
        """The authorities will
    commence the Kerala polytechnic online application process on the official
    website. Candidates have to visit the official website and complete the
    Kerala polytechnic registration process. They have to enter various details
    in the application form for Kerala polytechnic""",


    "admission",
        """The authorities will
    commence the Kerala polytechnic online application process on the official
    website. Candidates have to visit the official website and complete the
    Kerala polytechnic registration process. They have to enter various details
    in the application form for Kerala polytechnic""",


    "Please provide me with additional admission details",
    "http://gptcnedumkandam.ac.in/",
    
    "additional admission details",
    "http://gptcnedumkandam.ac.in/",
    
    "more admission details",
    "http://gptcnedumkandam.ac.in/",

    "admission details",
    "http://gptcnedumkandam.ac.in/",

    "What is the eligibility",
    """Candidates should be a native of
    Kerala and a citizen of India. The candidates applying should have
    qualified the SSLC or THSLC or any other exam equivalent from any other 
    board with Mathematics, English, and Science as their compulsory
    subjects""",

    "eligibility for apply/what is the qualification",
    """Candidates should be a native of
    Kerala and a citizen of India. The candidates applying should have
    qualified the SSLC or THSLC or any other exam equivalent from any other 
    board with Mathematics, English, and Science as their compulsory
    subjects""",


    "qualification for apply",
    """Candidates should be a native of
    Kerala and a citizen of India. The candidates applying should have
    qualified the SSLC or THSLC or any other exam equivalent from any other 
    board with Mathematics, English, and Science as their compulsory
    subjects""",


    ])

    rply=bot.get_response(qstn)
    # print(qstn)

    return rply