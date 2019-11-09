
public class Classification {
	String type;
	String category;
	
	public Classification(Object input) {
		category = (String) input;
		type = chooseType(category);
	}
	
	private String chooseType(String category) {
		if (!category.equals("trash")) {
			return "recycle";
		} else {
			return "trash";
		}
		//should deal with compost and mixed categories
	}
	
	public String getType() {
		return type;
	}
	
}
