// function sym(listOne, listTwo) {

//     newList = []

//     for (i = 0; i < listOne.length; i++){
//         if (listTwo.includes(listOne[i]) === false && newList.includes(listOne[i])===false)
//             newList.push(listOne[i])
//     }

//     for (i = 0; i < listTwo.length; i++){
//         if(listOne.includes(listTwo[i])=== false && newList.includes(listTwo[i])===false){
//             newList.push(listTwo[i])
//         }
//     }

    
//     newList = newList.sort()
    
//     console.log(newList)
//     return newList
// }

function sym(args) {
    var myArray = []; // Empty array, at first.
for (var i = 0; i < arguments.length; i++) {
    myArray.push(myArray[i])
}} // Now 'args' is an array that holds your arguments.
  
console.log(sym([1, 2, 3, 3], [5, 2, 1, 4]))

// [3, 4, 5]