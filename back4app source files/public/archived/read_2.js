const Guides = Parse.Object.extend("academic_planning_guides");
const guide = new Parse.Query(Guides);

guide.get("w8VabMPBFU")
.then((player) => {
  // The object was retrieved successfully.
}, (error) => {
  // The object was not retrieved successfully.
});