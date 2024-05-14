Parse.initialize("mKBbm0wXkcNolPQw1wkssxgCttS0gnjeThdCdXEt", "pvJCEZwSF3VVomRSt96w3hFwWNcYz32QiUBRrBKf"); //PASTE HERE YOUR Back4App APPLICATION ID AND YOUR JavaScript KEY
Parse.serverURL = "https://parseapi.back4app.com/";

read();

function read() {
    query = new Parse.Query(academic_planning_guides);
    query.equalTo("state_jurisdiction", textName);
    query.first().then(function(apg){
        if(apg){
           console.log('Pet found successful with name: ' + apg.get("state_jurisdiction") + ' and age: ' + apg.get("grade_range"));
        } else {
           console.log("Nothing found, please try again");
        }
    }).catch(function(error){
        console.log("Error: " + error.code + " " + error.message);       
    });