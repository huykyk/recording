public static class MyStack1{
	private Stack<Integer> stackData;
	private Stack<Integer> stackMin;

	public MyStack1(){
		this.stackData = new Stack<Integer>;
		this.stackMin = new Stack<Integer>;	
	}

	public void push(int newNum){
		if(this.stackMin.isEmpty()){
			this.stackMin.push(newNum);	
		}else if (newNum <= this.getMin()) {
			this.stackMin.push(newNum);
		}
		this.stackData.push(newNum);
	}
	public int pop(){
		if(this.stackData.isEmpty()){
			throw new RuntimeException("Your stack is empty.");
		}
		int value = this.stackData.pop();
		if(value == this.getMin()){
			this.stackMin.pop();
		}
		return value;
	}
	public int getMin(){
		if(this.stackMin.isEmpty()){
			throw new RuntimeException("Your stack is empty.");
		}
		return this.stackMin.peek();
	}
}