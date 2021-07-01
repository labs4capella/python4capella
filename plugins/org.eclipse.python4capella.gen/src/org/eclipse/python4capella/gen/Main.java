package org.eclipse.python4capella.gen;

import java.io.FileInputStream;
import java.io.IOException;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;
import javax.xml.xpath.XPath;
import javax.xml.xpath.XPathConstants;
import javax.xml.xpath.XPathExpressionException;
import javax.xml.xpath.XPathFactory;

import org.w3c.dom.Document;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;
import org.xml.sax.SAXException;

public class Main {

	public static void main(String[] args)
			throws IOException, ParserConfigurationException, SAXException, XPathExpressionException {
		FileInputStream fileIS = new FileInputStream("/tmp/report.xml");
		DocumentBuilderFactory builderFactory = DocumentBuilderFactory.newInstance();
		DocumentBuilder builder = builderFactory.newDocumentBuilder();
		Document xmlDocument = builder.parse(fileIS);
		XPath xPath = XPathFactory.newInstance().newXPath();
		String expression = "//*[contains(@message,'UnmodifiableEList')]/parent::testcase/@name";
		NodeList nodeList = (NodeList) xPath.compile(expression).evaluate(xmlDocument, XPathConstants.NODESET);

		for (int i = 0; i < nodeList.getLength(); i++) {
			Node node = nodeList.item(i);
			System.out.println(node.toString().replace("name=", "res.add(") + ");");
		}
	}

}
