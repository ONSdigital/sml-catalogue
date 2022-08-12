local help = import "help_centre.libsonnet";

{
   "view_methods":{
      "header3": help["categories"][0].label + ": " + help["categories"][0].subcategories[0].label,
      "guidances":[
         {
            "description":null,
            "details":[
               "You can find and view methods within the method_catalogue",
               "Content here from SML can be added.... "
            ],
            "hyper_link":{"method_catalogue":"/methods"}
         }
      ]
   },
   "methods_request":{
      "header3": help["categories"][0].label + ": " + help["categories"][0].subcategories[1].label,
      "guidances":[
         {
            "description":"How to make a method request:",
            "details":[
               "Instructions on how to use BAW and information about who can submit a method and the method governance process(whatever content SML team need to add …)",
               "For any reviews of the content added ( or to be pasted here in UI ...)"
            ],
            "hyper_link":{}
         },
         {
            "description":"How to change or update an existing method:",
            "details":[
               "Instructions on how to use BAW and information about who can submit a method and the method governance process(whatever content SML team need to add …)",
               "For any reviews of the content added ( or to be pasted here in UI ...)"
            ],
            "hyper_link":{}
         }    
      ]
   },
   "coding_standards":{
      "header3": help["categories"][0].label + ": " + help["categories"][0].subcategories[2].label,
      "guidances":[
         {
            "description":null,
            "details":[
               "Need DST input. link_here...",
               "Content here from SML team. This can be added by developers.... For any reviews of the content added ( or to be pasted here in UI ...)"
            ],
            "hyper_link":{"link_here":"/"}
         }  
      ]
   },
   "run_a_method":{
      "header3": help["categories"][1].label + ":" + help["categories"][1].subcategories[0].label,
      "guidances":[
         {
            "description":"How to run a method locally:",
            "details":[
               "Instructions and a link_here (whatever SML team need to add in and let the developers know the content...)",
               "For any reviews of the content added ( or to be pasted here in UI ...)"
            ],
            "hyper_link":{"link_here":"/"}
         },
         {
            "description":"How to run a method in IDS:",
            "details":[
               "Instructions and a link_here (whatever SML team need to add in and let the developers know the content...)",
               "For any reviews of the content added ( or to be pasted here in UI ...)"
            ],
            "hyper_link":{"link_here":"/"}
         }
      ]
   },
   "access_specification_code":{
      "header3": help["categories"][1].label + ":" + help["categories"][1].subcategories[1].label,
      "guidances":[
         {
            "description":'Accessing "public" method specification and code',
            "details":[
               "Fully public method code and specifications can be acccessed via a public GitHubRepo",
               "SML team to make content and developer to add here...",
               "For any reviews of the content added ( or to be pasted here in UI ...)"
            ],
            "hyper_link":{"GitHubRepo":"/"}
         },
         {
            "description":'Accessing "internal" method specification and code',
            "details":[
               "Instruction content here that provides hot to acccess an author-restricted method...)",
               "SML team to make content and developer to add here...",
               "For any reviews of the content added ( or to be pasted here in UI ...)"
            ],
            "hyper_link":{"link_here":"/"}
         }
      ]
   },
   "report_bug":{
      "header3": help["categories"][2].label + ":" + help["categories"][2].subcategories[0].label,
      "guidances":[
         {
            "description":null,
            "details":[
               "Instructions and a link_here (whatever SML team need to add in and let the developers know the content...)",
               "For any reviews of the content added ( or to be pasted here in UI ...)"
            ],
            "hyper_link":{"link_here":"/"}
         }
      ]
   },
   "provide_feedback":{
      "header3": help["categories"][2].label + ":" + help["categories"][2].subcategories[1].label,
      "guidances":[
          {
            "description":null,
            "details":[
               "Instructions and a link_here (whatever SML team need to add in and let the developers know the content...)",
               "For any reviews of the content added ( or to be pasted here in UI ...)"
            ],
            "hyper_link":{"link_here":"/"}
         }
      ]
   },
   "support":{
      "header3": help["categories"][3].label + ":" + help["categories"][3].subcategories[0].label,
      "guidances":[
         {
            "description": "Who to contact to ask for support with a method",
            "details":[
               "Instructions and a link_here (whatever SML team need to add in and let the developers know the content...)",
               "Conditions of support from Miro board(shoudl be used and added here...)",
               "For any reviews of the content added ( or to be pasted here in UI ...)"
            ],
            "hyper_link":{"link_here":"/"}
         }
      ]
   }
}