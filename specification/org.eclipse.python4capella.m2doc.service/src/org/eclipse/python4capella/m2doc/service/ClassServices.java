package org.eclipse.python4capella.m2doc.service;

import java.util.ArrayList;
import java.util.List;
import org.polarsys.capella.core.data.capellacore.GeneralizableElement;
import org.polarsys.capella.core.data.information.Class;
import org.polarsys.capella.core.data.information.Property;

public class ClassServices {

	public ClassServices() {
		// TODO Auto-generated constructor stub
	}
	
	public List<Class> getAllSuperTypes (Class myClass) {
		List<Class> result = new ArrayList<Class>();
		for (GeneralizableElement sup : myClass.getSuper()) {
			if (sup instanceof Class) {
				Class supClass = (Class) sup;
				for (Class supsupClass : getAllSuperTypes(supClass)) {
					if (!result.contains(supsupClass)) {
						result.add(supsupClass);
					}
				}
				if (!result.contains(supClass)) {
					result.add(supClass);
				}
			}
		}
		return result;
	}
	
	public List<Property> getAllAttributes (Class myClass) {
		List<Property> result = new ArrayList<Property>();
		for (Class supClass : getAllSuperTypes(myClass)) {
			result.addAll(getAttributes(supClass));
		}
		result.addAll(getAttributes(myClass));
		return result;
	}
	
	public List<Property> getAttributes (Class myClass) {
		List<Property> result = new ArrayList<Property>();
		for (Property prop : myClass.getContainedProperties()) {
			if (prop.getAssociation() == null) {
				result.add(prop);
			}
		}
		return result;
	}
	
	public List<Property> getAllRelations (Class myClass) {
		List<Property> result = new ArrayList<Property>();
		for (Class supClass : getAllSuperTypes(myClass)) {
			result.addAll(getRelations(supClass));
		}
		result.addAll(getRelations(myClass));
		return result;
	}
	
	public List<Property> getRelations (Class myClass) {
		List<Property> result = new ArrayList<Property>();
		for (Property prop : myClass.getContainedProperties()) {
			if (prop.getAssociation() != null) {
				result.add(prop);
			}
		}
		return result;
	}

}
