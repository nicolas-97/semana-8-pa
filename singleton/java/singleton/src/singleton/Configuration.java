package singleton;

public class Configuration {
	
	private static Configuration instance = null;
	private String option1;
    private String option2;
    
    private Configuration() {
    	this.option1 = "valor1";
        this.option2 = "valor2";
    }
    
    public static Configuration getInstance() {
    	if (instance == null) {
    		instance = new Configuration();
    	}
    	return instance;
    }
    
	public String getOption1() {
		return option1;
	}

	public void setOption1(String option1) {
		this.option1 = option1;
	}

	public String getOption2() {
		return option2;
	}

	public void setOption2(String option2) {
		this.option2 = option2;
	}
}
