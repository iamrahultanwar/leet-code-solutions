/**
 * @param {number[]} prices
 * @return {number}
 */
const Max = (a,b)=>{
    if(a > b){
        return a
    }
    return b
}
var maxProfit = function(prices) {
    let left = 0
    
    let result = 0
    
    for(let right=1;right < prices.length;right++){
        
        if(prices[right] < prices[left]){
            left = right
        }
        
        result = Max(result,prices[right]-prices[left])
    }
    
    return result
};