local help = import 'help_centre.libsonnet';

{
   "view_methods":{
      "header3": help['categories'][0].label + ": " + help['categories'][0].subcategories[0].label,
      "guidances":{
         "no_description":[
            {
               "text":"You can find and view methods within the methods catalogue"
            },
            {
               "text":"Content here from SML can be added.... "
            }
         ]
      }
   },
   "methods_request":{
      "header3": help['categories'][0].label + ": " + help['categories'][0].subcategories[1].label,
      "guidances":{
         "How to make a method request:":[
            {
               "text":"Instructions on how to use BAW and information about who can submit a method and the method governance process(whatever content SML team need to add …)"
            },
            {
               "text":"For any reviews of the content added ( or to be pasted here in UI ...)"
            }
         ],
         "How to change or update an existing method:":[
            {
               "text":"Instructions on how to use BAW and information about who can submit a method and the method governance process(whatever content SML team need to add …)"
            },
            {
               "text":"For any reviews of the content added ( or to be pasted here in UI ...)"
            }
         ]
      }
   },
   "coding_standards":{
      "header3": help['categories'][0].label + ": " + help['categories'][0].subcategories[2].label,
      "guidances":{
         "no_description":[
            {
               "text":"Need DST input..."
            },
            {
               "text":"Content here from SML team. This can be added by developers.... For any reviews of the content added ( or to be pasted here in UI ...)"
            }
         ]
      }
   },
      "run_a_method":{
      "header3": help['categories'][1].label + ":" + help['categories'][1].subcategories[0].label,
      "guidances":{
         "How to run a method locally:":[
            {
               "text":"Instructions and a link here (whatever SML team need to add in and let the developers know the content...)"
            },
            {
               "text":"For any reviews of the content added ( or to be pasted here in UI ...)"
            }
         ],
         "How to run a method in IDS:":[
            {
               "text":"Instructions and a link here (whatever SML team need to add in and let the developers know the content...)"
            },
            {
               "text":"For any reviews of the content added ( or to be pasted here in UI ...)"
            }
         ]
      }
   },
   "access_specification_code":{
      "header3": help['categories'][1].label + ":" + help['categories'][1].subcategories[1].label,
      "guidances":{
         "Accessing 'public' method specification and code":[
            {
               "text":"Fully public method code and specifications can be acccessed via a public GitHubRepo"
            },
            {
               "text":"SML team to make content and developer to add here..."
            },
            {
               "text":"For any reviews of the content added ( or to be pasted here in UI ...)"
            }
         ],
         "Accessing 'internal' method specification and code":[
            {
               "text":"Instruction content here that provides hot to acccess an author-restricted method...)"
            },
            {
               "text":"SML team to make content and developer to add here..."
            },
            {
               "text":"For any reviews of the content added ( or to be pasted here in UI ...)"
            }
         ]
      }
   },
    "report_bug":{
      "header3": help['categories'][2].label + ":" + help['categories'][2].subcategories[0].label,
      "guidances":{
         "no_description":[
            {
               "text":"Instructions and a link here (whatever SML team need to add in and let the developers know the content...)"
            },
            {
               "text":"For any reviews of the content added ( or to be pasted here in UI ...)"
            }
         ]
      }
   },
   "provide_feedback":{
      "header3": help['categories'][2].label + ":" + help['categories'][2].subcategories[1].label,
      "guidances":{
         "no_description":[
            {
               "text":"Instructions and a link here (whatever SML team need to add in and let the developers know the content...)"
            },
            {
               "text":"For any reviews of the content added ( or to be pasted here in UI ...)"
            }
         ]
      }
   },
   "support":{
      "header3": help['categories'][3].label + ":" + help['categories'][3].subcategories[0].label,
      "guidances":{
         "Who to contact to ask for support with a method":[
            {
               "text":"Instructions and a link here (whatever SML team need to add in and let the developers know the content...)"
            },
            {
               "text":"Conditions of support from Miro board(shoudl be used and added here...)"
            },
            {
               "text":"For any reviews of the content added ( or to be pasted here in UI ...)"
            }
         ]
      }
   }
}