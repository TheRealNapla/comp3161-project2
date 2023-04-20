USE BetterOurvle;
CREATE TABLE Courses (Course_id varchar(255),Coursename varchar(255), CourseLecturer varchar(255),Coursegrade int, PRIMARY KEY(Course_id));
INSERT INTO Courses (Course_id, Coursename, CourseLecturer, Coursegrade) VALUES
('SWEN276','Introduction to Artificial Intelligence for Beginners','Abigail Lopez','0'),('COMP135','Introduction to Artificial Intelligence using Java','Adam Sheppard','0'),('SWEN432','Advanced Cybersecurity in C++','Alejandra Townsend','0'),('COMP834','Applied Web Development for Beginners','Alexis Nunez','0'),('INFO572','Principles of Data Science for Professionals','Amber Griffith','0'),('COMP183','Exploring Cybersecurity with Python','Anthony Wolfe','0'),('INFO915','Introduction to Robotics for Professionals','Antonio Marquez','0'),('INFO980','Fundamentals of Robotics with Python','Benjamin Davis','0'),('COMP320','Introduction to Robotics for Beginners','Benjamin Luna','0'),('SOWK708','Research Methods in Geography in Contemporary Society','Bradley Wright','0'),('COMP048','Advanced Cloud Computing and Machine Learning','Brandon Martinez','0'),('SWEN651','Advanced Cybersecurity for Professionals','Brent Brennan','0'),('INFO831','Fundamentals of Artificial Intelligence using Java','Brett Mack','0'),('COMP803','Applied Data Science for Beginners','Brian Snyder','0'),('INFO730','Applied Cybersecurity with Python','Brooke Herrera','0'),('SOCI301','Research Methods in Anthropology in Contemporary Society','Carolyn Zhang','0'),('INFO738','Principles of Robotics with Python','Cassandra Martin','0'),('SWEN715','Introduction to Cybersecurity for Professionals','Cathy Garcia','0'),('SWEN237','Introduction to Robotics in C++','Christopher Elliott','0'),('COMP318','Principles of Cloud Computing for Professionals','Daniel Frazier','0'),('SOCI649','Research Methods in Anthropology for Professionals','Daniel Ramos','0'),('COMP576','Advanced Cybersecurity and Machine Learning','Danielle Soto','0'),('SOWK217','Foundations of Sociology in Global Perspective','Darlene Copeland','0'),('SOCI616','Key Concepts in Economics in Global Perspective','David Miller','0'),('INFO548','Applied Robotics for Beginners','Debbie Owens','0'),('GOVT252','Foundations of Political Science for Beginners','Douglas Kim','0'),('COMP331','Principles of Web Development in C++','Eric Bishop','0'),('INFO332','Exploring Cybersecurity for Professionals','Eric Caldwell','0'),('GOVT349','Introduction to Geography for Beginners','Erica Massey','0'),('SWEN978','Applied Artificial Intelligence in C++','Ethan Brown','0'),('SOCI224','Introduction to Anthropology for Professionals','Gregory Clark','0'),('COMP154','Fundamentals of Cybersecurity in C++','Harold Wells','0'),('SWEN815','Advanced Robotics in C++','Helen Sanchez','0'),('SOWK189','Comparative Studies of Economics for Professionals','Holly Ross','0'),('SOWK981','Comparative Studies of Anthropology in Global Perspective','James Holt','0'),('COMP689','Exploring Robotics for Beginners','James Marshall','0'),('COMP862','Introduction to Data Science and Machine Learning','James Parker','0'),('SOCI770','Theories of Sociology for Professionals','Janet Leon','0'),('SOWK893','Key Concepts in Political Science in Global Perspective','Jasmine Long','0'),('SOCI124','Theories of Psychology for Advanced Students','Jason Farrell','0'),('INFO089','Advanced Web Development and Machine Learning','Jason Hernandez','0'),('SOWK612','Key Concepts in Sociology for Beginners','Jeffrey Lozano','0'),('INFO205','Principles of Robotics using Java','Jennifer Baxter','0'),('SOWK745','Foundations of Anthropology in Contemporary Society','Jennifer Collins','0'),('SWEN493','Advanced Robotics with Python','Jennifer Hicks','0'),('SOCI144','Foundations of Economics for Advanced Students','Jermaine Ford','0'),('SWEN391','Introduction to Data Science in C++','Jessica Stephens','0'),('SOCI535','Introduction to Economics in Global Perspective','Joanna Murphy','0'),('SWEN064','Fundamentals of Artificial Intelligence in C++','John Becker','0'),('SOWK243','Comparative Studies of Anthropology for Professionals','Jon Navarro','0'),('SWEN667','Applied Data Science in C++','Joseph Schroeder','0'),('SOCI992','Comparative Studies of Psychology in Global Perspective','Joshua Duran','0'),('INFO136','Principles of Cybersecurity with Python','Joshua Johnson','0'),('GOVT030','Theories of Sociology for Beginners','Julia Williams','0'),('GOVT231','Research Methods in Economics for Advanced Students','Julie Ramos','0'),('COMP793','Applied Robotics and Machine Learning','Karen Weeks','0'),('GOVT292','Research Methods in Sociology in Contemporary Society','Kathleen Frazier','0'),('SWEN210','Principles of Robotics for Beginners','Kelsey Morales','0'),('SOCI846','Foundations of Sociology for Beginners','Kenneth Sherman','0'),('COMP601','Principles of Web Development using Java','Kenneth Smith','0'),('COMP077','Exploring Web Development in C++','Kristin Wright','0'),('SOCI341','Theories of Psychology in Global Perspective','Kyle Cummings','0'),('SOCI427','Key Concepts in Economics for Advanced Students','Leslie Harrison','0'),('SWEN825','Advanced Artificial Intelligence in C++','Lisa Perkins','0'),('COMP837','Advanced Web Development for Professionals','Marcus Cobb','0'),('SOCI781','Key Concepts in Psychology for Professionals','Maria Wolfe','0'),('SOCI178','Foundations of Economics for Beginners','Mark Lopez','0'),('GOVT702','Research Methods in Sociology for Advanced Students','Mary Baker','0'),('INFO397','Applied Robotics for Professionals','Matthew Castro','0'),('SOCI336','Introduction to Sociology for Advanced Students','Melinda Johnson','0'),('SWEN284','Applied Cloud Computing and Machine Learning','Melissa Bennett','0'),('COMP446','Applied Cybersecurity and Machine Learning','Michael Larsen','0'),('SOCI706','Key Concepts in Geography in Contemporary Society','Michelle Howard','0'),('SOCI411','Comparative Studies of Economics for Beginners','Morgan Mendoza','0'),('SWEN158','Introduction to Robotics with Python','Nathan Reyes','0'),('SOWK129','Comparative Studies of Sociology for Advanced Students','Patricia Davis','0'),('SWEN070','Advanced Web Development in C++','Paula Smith','0'),('INFO710','Principles of Data Science for Beginners','Priscilla Bond','0'),('GOVT503','Introduction to Psychology in Global Perspective','Rachel Scott','0'),('SWEN935','Exploring Data Science in C++','Rebecca Wilson','0'),('SOWK146','Theories of Anthropology in Contemporary Society','Rhonda Carlson','0'),('INFO720','Fundamentals of Data Science using Java','Robert Alexander','0'),('SOCI670','Theories of Sociology in Global Perspective','Robert Allison','0'),('SWEN131','Exploring Robotics with Python','Robert Crosby','0'),('SOCI978','Research Methods in Anthropology for Advanced Students','Roger Ayala','0'),('SWEN965','Fundamentals of Data Science for Beginners','Ryan Young','0'),('GOVT501','Introduction to Political Science in Global Perspective','Samuel Alexander','0'),('SWEN559','Fundamentals of Cloud Computing and Machine Learning','Sandra Wiggins','0'),('COMP149','Exploring Artificial Intelligence for Beginners','Scott Carter','0'),('SOCI683','Comparative Studies of Geography for Beginners','Scott Olson','0'),('SOCI317','Theories of Political Science for Professionals','Scott Thomas','0'),('GOVT493','Key Concepts in Sociology for Professionals','Spencer Vargas','0'),('COMP376','Fundamentals of Artificial Intelligence for Beginners','Stephen Roberts','0'),('GOVT519','Foundations of Psychology for Beginners','Susan Thomas','0'),('SWEN885','Fundamentals of Robotics in C++','Thomas Powell','0'),('SOWK738','Foundations of Geography for Professionals','Timothy Cook','0'),('SOWK460','Key Concepts in Geography in Global Perspective','Timothy Meza','0'),('INFO767','Exploring Cloud Computing for Beginners','Travis Gallagher','0'),('SOCI786','Research Methods in Sociology for Professionals','Vincent Lopez','0'),('COMP016','Exploring Data Science for Beginners','Wayne Watkins','0'),('SWEN770','Fundamentals of Artificial Intelligence for Professionals','Kristin Wright','0'),('SOCI337','Research Methods in Political Science for Professionals','Kyle Cummings','0'),('GOVT769','Key Concepts in Sociology in Contemporary Society','Leslie Harrison','0'),('COMP275','Introduction to Cybersecurity for Beginners','Lisa Perkins','0'),('GOVT999','Key Concepts in Economics for Professionals','Marcus Cobb','0'),('SWEN343','Principles of Data Science with Python','Maria Wolfe','0'),('SOCI112','Foundations of Psychology in Contemporary Society','Mark Lopez','0'),('COMP133','Exploring Robotics for Professionals','Mary Baker','0'),('SOCI627','Foundations of Geography for Advanced Students','Matthew Castro','0'),('INFO825','Exploring Cloud Computing and Machine Learning','Melinda Johnson','0'),('INFO127','Fundamentals of Data Science for Professionals','Melissa Bennett','0'),('SOWK577','Comparative Studies of Economics for Advanced Students','Michael Larsen','0'),('GOVT242','Research Methods in Psychology in Global Perspective','Michelle Howard','0'),('INFO683','Advanced Robotics for Professionals','Morgan Mendoza','0'),('COMP047','Fundamentals of Robotics and Machine Learning','Nathan Reyes','0'),('SOCI747','Key Concepts in Geography for Beginners','Patricia Davis','0'),('INFO151','Applied Web Development with Python','Paula Smith','0'),('GOVT786','Comparative Studies of Anthropology in Contemporary Society','Priscilla Bond','0'),('COMP011','Introduction to Web Development for Beginners','Rachel Scott','0'),('SOWK173','Key Concepts in Geography for Advanced Students','Rebecca Wilson','0'),('GOVT833','Theories of Political Science for Beginners','Rhonda Carlson','0'),('SWEN979','Fundamentals of Data Science in C++','Robert Alexander','0'),('SWEN239','Fundamentals of Cloud Computing in C++','Robert Allison','0'),('GOVT088','Research Methods in Geography for Professionals','Robert Crosby','0'),('SOWK549','Introduction to Sociology in Global Perspective','Roger Ayala','0'),('SWEN617','Advanced Robotics and Machine Learning','Ryan Young','0'),('SOCI105','Key Concepts in Economics for Beginners','Samuel Alexander','0'),('SWEN566','Advanced Cloud Computing for Professionals','Sandra Wiggins','0'),('COMP012','Advanced Web Development using Java','Scott Carter','0'),('SOWK294','Key Concepts in Anthropology in Global Perspective','Scott Olson','0'),('SOWK196','Introduction to Political Science for Professionals','Scott Thomas','0'),('GOVT679','Comparative Studies of Psychology for Advanced Students','Spencer Vargas','0'),('INFO995','Applied Artificial Intelligence for Beginners','Stephen Roberts','0'),('SOWK809','Comparative Studies of Anthropology for Beginners','Susan Thomas','0'),('SWEN674','Applied Data Science for Professionals','Thomas Powell','0'),('SOCI326','Key Concepts in Psychology in Global Perspective','Timothy Cook','0'),('SWEN384','Fundamentals of Web Development for Professionals','Timothy Meza','0'),('GOVT094','Key Concepts in Anthropology for Advanced Students','Brian Snyder','0'),('SOWK386','Theories of Economics for Professionals','Brooke Herrera','0'),('SWEN415','Introduction to Cloud Computing using Java','Carolyn Zhang','0'),('SOWK496','Research Methods in Geography for Beginners','Cassandra Martin','0'),('COMP343','Advanced Data Science using Java','Cathy Garcia','0'),('INFO037','Introduction to Data Science for Professionals','Christopher Elliott','0'),('GOVT557','Comparative Studies of Political Science for Professionals','Daniel Frazier','0'),('SWEN701','Exploring Data Science using Java','Daniel Ramos','0'),('INFO370','Exploring Cybersecurity using Java','Danielle Soto','0'),('GOVT609','Research Methods in Political Science for Beginners','Darlene Copeland','0'),('SWEN324','Applied Cybersecurity for Beginners','David Miller','0'),('GOVT009','Introduction to Geography for Advanced Students','Debbie Owens','0'),('COMP109','Principles of Cloud Computing using Java','Douglas Kim','0'),('SWEN496','Advanced Artificial Intelligence with Python','Eric Bishop','0'),('INFO168','Applied Cloud Computing for Beginners','Eric Caldwell','0'),('SWEN141','Advanced Robotics using Java','Erica Massey','0'),('SOCI020','Theories of Geography for Professionals','Ethan Brown','0'),('SWEN273','Fundamentals of Cloud Computing with Python','Gregory Clark','0'),('COMP955','Advanced Data Science for Beginners','Harold Wells','0'),('INFO086','Advanced Web Development with Python','Helen Sanchez','0'),('COMP727','Fundamentals of Cybersecurity for Beginners','Holly Ross','0'),('COMP369','Introduction to Web Development with Python','James Holt','0'),('SWEN714','Advanced Artificial Intelligence and Machine Learning','James Marshall','0'),('INFO797','Applied Data Science using Java','James Parker','0'),('SWEN259','Fundamentals of Data Science and Machine Learning','Janet Leon','0'),('COMP995','Principles of Cloud Computing with Python','Jasmine Long','0'),('COMP365','Introduction to Cloud Computing in C++','Jason Farrell','0'),('COMP268','Principles of Web Development for Beginners','Jason Hernandez','0'),('INFO627','Applied Web Development and Machine Learning','Jeffrey Lozano','0'),('INFO219','Exploring Cloud Computing with Python','Jennifer Baxter','0'),('COMP518','Applied Web Development using Java','Jennifer Collins','0'),('SOCI373','Research Methods in Sociology in Global Perspective','Jennifer Hicks','0'),('COMP459','Applied Cloud Computing in C++','Jermaine Ford','0'),('COMP674','Principles of Cybersecurity for Beginners','Jessica Stephens','0'),('SOWK110','Foundations of Sociology for Professionals','Joanna Murphy','0'),('GOVT221','Comparative Studies of Geography for Professionals','John Becker','0'),('SWEN268','Exploring Cybersecurity in C++','Jon Navarro','0'),('GOVT998','Comparative Studies of Psychology in Contemporary Society','Joseph Schroeder','0'),('SWEN454','Fundamentals of Robotics using Java','Joshua Duran','0'),('SWEN639','Exploring Web Development for Professionals','Joshua Johnson','0'),('SWEN418','Introduction to Cybersecurity and Machine Learning','Julia Williams','0'),('SWEN196','Applied Cybersecurity using Java','Julie Ramos','0'),('SWEN600','Exploring Web Development using Java','Karen Weeks','0'),('SOCI554','Comparative Studies of Political Science in Contemporary Society','Kathleen Frazier','0'),('INFO062','Fundamentals of Cybersecurity with Python','Kelsey Morales','0'),('SWEN653','Introduction to Data Science for Beginners','Kenneth Sherman','0'),('COMP267','Principles of Robotics for Professionals','Kenneth Smith','0'),('SOWK667','Theories of Anthropology for Professionals','Abigail Lopez','0'),('SOCI160','Comparative Studies of Sociology in Global Perspective','Adam Sheppard','0'),('SWEN296','Advanced Cybersecurity for Beginners','Alejandra Townsend','0'),('SWEN957','Introduction to Artificial Intelligence in C++','Alexis Nunez','0'),('SWEN100','Advanced Cloud Computing with Python','Amber Griffith','0'),('COMP876','Advanced Artificial Intelligence using Java','Anthony Wolfe','0'),('SWEN050','Introduction to Data Science using Java','Antonio Marquez','0'),('SOWK035','Introduction to Geography in Contemporary Society','Benjamin Davis','0'),('GOVT911','Theories of Psychology in Contemporary Society','Benjamin Luna','0'),('INFO105','Exploring Robotics using Java','Bradley Wright','0'),('SOWK980','Comparative Studies of Geography in Contemporary Society','Brandon Martinez','0'),('COMP778','Principles of Data Science using Java','Brent Brennan','0'),('SOCI080','Comparative Studies of Sociology in Contemporary Society','Brett Mack','0'),('INFO888','Principles of Cloud Computing for Beginners','Rachel Scott','0'),('COMP994','Principles of Cloud Computing and Machine Learning','Rebecca Wilson','0'),('SOWK249','Foundations of Anthropology for Advanced Students','Rhonda Carlson','0'),('INFO264','Exploring Artificial Intelligence and Machine Learning','Robert Alexander','0'),('COMP270','Applied Artificial Intelligence for Professionals','Robert Allison','0'),('INFO396','Principles of Cybersecurity for Professionals','Robert Crosby','0'),('COMP155','Principles of Artificial Intelligence using Java','Roger Ayala','0'),('INFO353','Principles of Cybersecurity and Machine Learning','Ryan Young','0'),('COMP848','Introduction to Cloud Computing for Professionals','Samuel Alexander','0'),('COMP680','Exploring Cybersecurity for Beginners','Sandra Wiggins','0'),('SWEN241','Applied Artificial Intelligence and Machine Learning','Scott Carter','0'),('COMP682','Principles of Artificial Intelligence for Professionals','Scott Olson','0');