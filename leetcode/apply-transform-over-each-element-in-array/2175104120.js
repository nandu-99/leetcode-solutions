/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    let ans = [];
    arr.forEach((ele, i)=>{
        ans.push(fn(ele,i))
    })
    return ans
};