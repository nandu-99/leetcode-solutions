/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    let filteredArr = []
    arr.forEach((ele, index)=>{
        if(fn(ele, index)){
            filteredArr.push(ele)
        }
    })
    return filteredArr;
};