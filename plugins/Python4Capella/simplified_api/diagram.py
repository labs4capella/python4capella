'''
Created on 11 july 2025

@author: <a href="mailto:yvan.lussaud@obeo.fr">Yvan Lussaud</a>
'''
# include needed for the Capella modeller API
from typing import Dict
include('workspace://Python4Capella/simplified_api/capella.py')
if False:
    from simplified_api.capella import *

# Mapping EClasses
mappingEClass = get_e_classifier("http://www.eclipse.org/sirius/description/1.1.0", "RepresentationElementMapping")
containerMappingEClass = get_e_classifier("http://www.eclipse.org/sirius/diagram/description/1.1.0", "ContainerMapping")
nodeMappingEClass = get_e_classifier("http://www.eclipse.org/sirius/diagram/description/1.1.0", "NodeMapping")
edgeMappingEClass = get_e_classifier("http://www.eclipse.org/sirius/diagram/description/1.1.0", "EdgeMapping")

# Style Description EClasses
flatContainerStyleDescriptionEClass = get_e_classifier("http://www.eclipse.org/sirius/diagram/description/style/1.1.0", "FlatContainerStyleDescription")
shapeContainerStyleDescriptionEClass = get_e_classifier("http://www.eclipse.org/sirius/diagram/description/style/1.1.0", "ShapeContainerStyleDescription")
workspaceImageDescriptionEClass = get_e_classifier("http://www.eclipse.org/sirius/diagram/description/style/1.1.0", "WorkspaceImageDescription")

bundledImageDescriptionEClass = get_e_classifier("http://www.eclipse.org/sirius/diagram/description/style/1.1.0", "BundledImageDescription")
customStyleDescriptionEClass = get_e_classifier("http://www.eclipse.org/sirius/diagram/description/style/1.1.0", "CustomStyleDescription")
dotDescriptionEClass = get_e_classifier("http://www.eclipse.org/sirius/diagram/description/style/1.1.0", "DotDescription")
ellipseNodeDescriptionEClass = get_e_classifier("http://www.eclipse.org/sirius/diagram/description/style/1.1.0", "EllipseNodeDescription")
gaugeCompositeStyleDescriptionEClass = get_e_classifier("http://www.eclipse.org/sirius/diagram/description/style/1.1.0", "GaugeCompositeStyleDescription")
lozengeNodeDescriptionEClass = get_e_classifier("http://www.eclipse.org/sirius/diagram/description/style/1.1.0", "LozengeNodeDescription")
NoteDescriptionEClass = get_e_classifier("http://www.eclipse.org/sirius/diagram/description/style/1.1.0", "NoteDescription")
squareDescriptionEClass = get_e_classifier("http://www.eclipse.org/sirius/diagram/description/style/1.1.0", "SquareDescription")
workspaceImageDescriptionEClass = get_e_classifier("http://www.eclipse.org/sirius/diagram/description/style/1.1.0", "WorkspaceImageDescription")

bracketEdgeStyleDescriptionEClass = get_e_classifier("http://www.eclipse.org/sirius/diagram/description/style/1.1.0", "BracketEdgeStyleDescription")
edgeStyleDescriptionEClass = get_e_classifier("http://www.eclipse.org/sirius/diagram/description/style/1.1.0", "EdgeStyleDescription")

# # Diagram EClasses

# Element EClasses
dDiagramEClass = get_e_classifier("http://www.eclipse.org/sirius/diagram/1.1.0", "DDiagram")
dNodeContainerEClass = get_e_classifier("http://www.eclipse.org/sirius/diagram/1.1.0", "DNodeContainer")
dNodeEClass = get_e_classifier("http://www.eclipse.org/sirius/diagram/1.1.0", "DNode")
dEdgeEClass = get_e_classifier("http://www.eclipse.org/sirius/diagram/1.1.0", "DEdge")

# Style EClasses
flatContainerStyleEClass = get_e_classifier("http://www.eclipse.org/sirius/diagram/1.1.0", "FlatContainerStyle")
shapeContainerStyleEClass = get_e_classifier("http://www.eclipse.org/sirius/diagram/1.1.0", "ShapeContainerStyle")
workspaceImageEClass = get_e_classifier("http://www.eclipse.org/sirius/diagram/1.1.0", "WorkspaceImage")

bundledImageEClass = get_e_classifier("http://www.eclipse.org/sirius/diagram/1.1.0", "BundledImage")
customStyleEClass = get_e_classifier("http://www.eclipse.org/sirius/diagram/1.1.0", "CustomStyle")
dotEClass = get_e_classifier("http://www.eclipse.org/sirius/diagram/1.1.0", "Dot")
ellipseNodeEClass = get_e_classifier("http://www.eclipse.org/sirius/diagram/1.1.0", "EllipseNode")
gaugeCompositeStyleEClass = get_e_classifier("http://www.eclipse.org/sirius/diagram/1.1.0", "GaugeCompositeStyle")
lozengeNodeEClass = get_e_classifier("http://www.eclipse.org/sirius/diagram/1.1.0", "LozengeNode")
NoteEClass = get_e_classifier("http://www.eclipse.org/sirius/diagram/1.1.0", "Note")
squareEClass = get_e_classifier("http://www.eclipse.org/sirius/diagram/1.1.0", "Square")
workspaceImageEClass = get_e_classifier("http://www.eclipse.org/sirius/diagram/1.1.0", "WorkspaceImage")

bracketEdgeStyleEClass = get_e_classifier("http://www.eclipse.org/sirius/diagram/1.1.0", "BracketEdgeStyle")
edgeStyleEClass = get_e_classifier("http://www.eclipse.org/sirius/diagram/1.1.0", "EdgeStyle")

# GMF Notation EClasses
nodeEClass = get_e_classifier("http://www.eclipse.org/gmf/runtime/1.0.3/notation", "Node")
edgeEClass = get_e_classifier("http://www.eclipse.org/gmf/runtime/1.0.3/notation", "Edge")

boundsEClass = get_e_classifier("http://www.eclipse.org/gmf/runtime/1.0.3/notation", "Bounds")

# Gets the representation definition by its name.
# session is the Java Object session from the CapellaModel.session for instance
def get_representation_definition_by_name(session, name):
    for viewpoint in JavaList(java.util.ArrayList(session.getSelectedViewpoints(True)), EObject):
        for representation_definition in viewpoint.get_java_object().getOwnedRepresentations():
            if representation_definition.getName() == name:
                return representation_definition
    return None

# Gets the representation mapping by its name
# representationDefinition is the Java Object you can retrieve with get_representation_definition_by_name(session, name) for instance
def get_representation_mapping_by_name(representationDefinition, name):
    for content in JavaList(eAllContentsByType(representationDefinition, mappingEClass), EObject):
        if content.get_java_object().getName() == name:
            return content.get_java_object()
    return None

# Create the style corresponding to the given mapping
# mapping is the Java Object you can retrieve with get_representation_mapping_by_name(representationDefinition, name) for instance
def create_style(mapping):
    res = None
    style_description = mapping.getStyle()
    if flatContainerStyleDescriptionEClass.isInstance(style_description):
        res = create_e_object_from_e_classifier(flatContainerStyleEClass)
    elif shapeContainerStyleDescriptionEClass.isInstance(style_description):
        res = create_e_object_from_e_classifier(shapeContainerStyleEClass)
    elif workspaceImageDescriptionEClass.isInstance(style_description):
        res = create_e_object_from_e_classifier(workspaceImageEClass)
    elif workspaceImageDescriptionEClass.isInstance(style_description):
        res = create_e_object_from_e_classifier(workspaceImageEClass)
    elif bundledImageDescriptionEClass.isInstance(style_description):
        res = create_e_object_from_e_classifier(bundledImageEClass)
    elif customStyleDescriptionEClass.isInstance(style_description):
        res = create_e_object_from_e_classifier(customStyleEClass)
    elif dotDescriptionEClass.isInstance(style_description):
        res = create_e_object_from_e_classifier(dotEClass)
    elif ellipseNodeDescriptionEClass.isInstance(style_description):
        res = create_e_object_from_e_classifier(ellipseNodeEClass)
    elif gaugeCompositeStyleDescriptionEClass.isInstance(style_description):
        res = create_e_object_from_e_classifier(gaugeCompositeStyleEClass)
    elif lozengeNodeDescriptionEClass.isInstance(style_description):
        res = create_e_object_from_e_classifier(lozengeNodeEClass)
    elif NoteDescriptionEClass.isInstance(style_description):
        res = create_e_object_from_e_classifier(NoteEClass)
    elif squareDescriptionEClass.isInstance(style_description):
        res = create_e_object_from_e_classifier(squareEClass)
    elif workspaceImageDescriptionEClass.isInstance(style_description):
        res = create_e_object_from_e_classifier(workspaceImageEClass)
    elif bracketEdgeStyleDescriptionEClass.isInstance(style_description):
        res = create_e_object_from_e_classifier(bracketEdgeStyleEClass)
    elif edgeStyleDescriptionEClass.isInstance(style_description):
        res = create_e_object_from_e_classifier(edgeStyleEClass)
    else:
        raise ValueError("Unkonw style description " + style_description.eClass().getName())

    return res

# Creates a represenation element for the given mapping and EObject semantic element
# mapping is the Java Object you can retrieve with get_representation_mapping_by_name(representationDefinition, name) for instance
# eObj is the Java Object from the Capella model for instance
def create_representation_element(mapping, eObj):
    res = None
    if containerMappingEClass.isInstance(mapping):
        res = create_e_object_from_e_classifier(dNodeContainerEClass)
    elif nodeMappingEClass.isInstance(mapping):
        res = create_e_object_from_e_classifier(dNodeEClass)
    elif edgeMappingEClass.isInstance(mapping):
        res = create_e_object_from_e_classifier(dEdgeEClass)
    else:
        raise AttributeError("don't know how to create representation element for mapping" + mapping.eClass().getName())

    res.setActualMapping(mapping)
    res.setTarget(eObj)
    res.getSemanticElements().add(eObj)

    return res

# Applies the given mapping on the given EObject semantic element. It can also applies some style customizations
# container the Java Object representation element (DDiagram, DNodeContainer, ...) that will contain the created representation element
# eObj is the Java Object from the Capella model for instance
# customizations the mapping from the customized style feature name to its value (for instance "size" -> 4)
def apply_mapping(container, mapping, eObj, customizations: Dict[str, Any] = None):
    representationElement = create_representation_element(mapping, eObj)
    if customizations:
        style = representationElement.getOwnedStyle()
        if not style:
            style = create_style(mapping)
            representationElement.setOwnedStyle(style)
        customize_style(style, customizations)

    if dNodeContainerEClass.isInstance(container):
        if container.getActualMapping().getBorderedNodeMappings().contains(mapping) or container.getActualMapping().getReusedBorderedNodeMappings().contains(mapping):
            container.getOwnedBorderedNodes().add(representationElement)
        else:
            container.getOwnedDiagramElements().add(representationElement)
    elif dDiagramEClass.isInstance(container):
        container.getOwnedDiagramElements().add(representationElement)
    else:
        raise AttributeError("don't know how to add to " + container.toString())

    return representationElement

# Create the representation for the given semantic element and representation definition
# session is the Java Object session from the CapellaModel.session for instance
# eObj is the Python Object from the Capella model for instance
# representationDefinition is the Java Object you can retrieve with get_representation_definition_by_name(session, name) for instance
# representation_name the created representation name
def create_representation(session, semantic_element, representationDefinition, representation_name):
    monitor = org.eclipse.core.runtime.NullProgressMonitor()
    dialectManager = org.eclipse.sirius.business.api.dialect.DialectManager.INSTANCE
    newRepresentation = dialectManager.createRepresentation(representation_name, semantic_element.get_java_object(), representationDefinition, session, monitor)
    return newRepresentation

# Customizes the given style
# style the Java Object style of a representation element (for instance representationElement.getOwnedStyle())
# customizations the mapping from the customized style feature name to its value (for instance "size" -> 4)
def customize_style(style, customizations: Dict[str, Any]):
    for featureName, value in customizations.items():
        feature = style.eClass().getEStructuralFeature(featureName)
        if not feature:
            ValueError("can't customize feature '" + featureName + "' not found. Available features are " + [feature.getName() for feature in style.eClass().getEAllStructuralFeatures()])
        else:
            style.eSet(feature, value)
            if not style.getCustomFeatures().contains(featureName):
                style.getCustomFeatures().add(featureName)


# Gets the bounds of a diagram element
# diagramElement a Java Object representation element form a diagram representation
# returns [x, y, width, height]
def get_bounds(diagramElement) -> List[int]:
    nodes = eInverseByType(diagramElement, nodeEClass)
    if len(nodes) > 0:
        res = []
        bounds = nodes[0].getLayoutConstraint()
        res.append(bounds.getX())
        res.append(bounds.getY())
        res.append(bounds.getWidth())
        res.append(bounds.getHeight())
        return res
    else:
        raise ValueError("the given diagram element has no GMF node.")
    
# Sets the bounds of a representation element form a diagram representation
# diagramElement a Java Object representation element form a diagram representation
# values [x, y, width, height]
def set_bounds(diagramElement, dimensions: List[int]):
    nodes = eInverseByType(diagramElement, nodeEClass)
    if len(nodes) > 0:
        bounds = nodes[0].getLayoutConstraint()
        bounds.setX(dimensions[0])
        bounds.setY(dimensions[1])
        bounds.setWidth(dimensions[2])
        bounds.setHeight(dimensions[3])
    else:
        raise ValueError("the given diagram element has no GMF node.")

# Hides the given diagram element
# you can get diagram elements using myDiagram.get_java_obect().getRepresentation().getRepresentationElements()
def hide(diagramElement):
    org.eclipse.sirius.diagram.business.api.helper.graphicalfilters.HideFilterHelper.INSTANCE.hide(diagramElement)


# Reveals the given diagram element
# you can get diagram elements using myDiagram.get_java_obect().getRepresentation().getRepresentationElements()
def reveal(diagramElement):
    org.eclipse.sirius.diagram.business.api.helper.graphicalfilters.HideFilterHelper.INSTANCE.reveal(diagramElement)

# set the style of the given DiagramElement as an image form the workspace
def set_workspace_image(diagramElement, image_path):
    style = diagramElement.getOwnedStyle()
    helper = org.eclipse.sirius.diagram.ui.business.api.image.WorkspaceImageHelper()
    helper.updateStyle(style, image_path)
