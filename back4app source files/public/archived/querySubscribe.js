var query = new Parse.Query('academic_planning_guides');
query.ascending('createdAt').limit(5);
var subscription = client.subscribe(query);
