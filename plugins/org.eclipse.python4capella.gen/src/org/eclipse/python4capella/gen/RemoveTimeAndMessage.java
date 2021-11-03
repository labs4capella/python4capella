package org.eclipse.python4capella.gen;

import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;
import javax.xml.transform.OutputKeys;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerConfigurationException;
import javax.xml.transform.TransformerException;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.TransformerFactoryConfigurationError;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;

import org.w3c.dom.Node;
import org.w3c.dom.NodeList;
import org.xml.sax.SAXException;

public class RemoveTimeAndMessage {

	public static void main(String[] args) {

		for (String fileName : args) {
			DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
			factory.setNamespaceAware(true);
			org.w3c.dom.Document doc = null;
			NodeList nodes = null;
			try {
				DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
				DocumentBuilder db = dbf.newDocumentBuilder();
				doc = db.parse(fileName);
				nodes = doc.getChildNodes();
				stripTimedMessage(nodes);
			} catch (IOException e) {
				e.printStackTrace();
			} catch (ParserConfigurationException e) {
				e.printStackTrace();
			} catch (SAXException e) {
				e.printStackTrace();
			}
			Transformer transformer;
			StreamResult result = null;
			try {
				transformer = TransformerFactory.newInstance().newTransformer();
				transformer.setOutputProperty(OutputKeys.INDENT, "yes");
				result = new StreamResult(new FileOutputStream(fileName + "-out.txt"));
				DOMSource source = new DOMSource(doc);
				transformer.transform(source, result);
			} catch (TransformerConfigurationException e) {
				e.printStackTrace();
			} catch (TransformerFactoryConfigurationError e) {
				e.printStackTrace();
			} catch (TransformerException e) {
				e.printStackTrace();
			} catch (FileNotFoundException e) {
				e.printStackTrace();
			}
		}
	}

	private static void stripTimedMessage(NodeList nodes) {
		for (int i = 0; i < nodes.getLength(); i++) {
			final Node child = nodes.item(i);
			if (child.hasAttributes() && child.getAttributes().getNamedItem("time") != null) {
				child.getAttributes().removeNamedItem("time");
			}
			if (child.hasAttributes() && child.getAttributes().getNamedItem("message") != null) {
				child.getAttributes().removeNamedItem("message");
			}
			stripTimedMessage(child.getChildNodes());
		}
	}
}