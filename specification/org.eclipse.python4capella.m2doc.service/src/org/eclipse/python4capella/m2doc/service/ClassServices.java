package org.eclipse.python4capella.m2doc.service;

import java.util.ArrayList;
import java.util.List;

import org.eclipse.emf.common.util.TreeIterator;
import org.eclipse.emf.ecore.EObject;
import org.polarsys.capella.core.data.capellacore.GeneralizableElement;
import org.polarsys.capella.core.data.capellamodeller.SystemEngineering;
import org.polarsys.capella.core.data.information.AggregationKind;
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
	
	public List<Class> getPossibleParents (Class myClass) {
		List<Class> result = new ArrayList<Class>();
		List<Class> target = new ArrayList<Class>();
		target.addAll(getAllSuperTypes(myClass));
		target.add(myClass);
		SystemEngineering se = getSE(myClass);
		if (se != null) {
			TreeIterator<EObject> it = se.eAllContents();
			while (it.hasNext()) {
				EObject obj = it.next();
				if (obj instanceof Class) {
					Class currentClass = (Class) obj;
					if (!currentClass.isAbstract()) {
						for (Property rel : getAllRelations(currentClass)) {
							if (rel.getAggregationKind() == AggregationKind.COMPOSITION) {
								if (target.contains(rel.getType())) {
									result.add(currentClass);
								}
							}
						}
					}
				}
			}
		}
		return result;
	}
	
	private SystemEngineering getSE(EObject obj) {
		if (obj instanceof SystemEngineering) {
			return (SystemEngineering) obj;
		}
		if (obj.eContainer() != null) {
			return getSE(obj.eContainer());
		}
		return null;
	}

}
