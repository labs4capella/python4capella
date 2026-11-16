var __EASE_UnitTest_TestRunner = {

		easeModule : loadModule("/Unittest", true),

		/**
		 * Execute all unit tests.
		 */
		run : function() {
			this.easeModule.javaInstance.setThrowOnFailure(true);

			var iterator = getScriptEngine().getVariables().entrySet().iterator();
			while (iterator.hasNext()) {
				var candidateEntry = iterator.next();
				var candidate = candidateEntry.getValue();
				if (this.isUnitTest(candidateEntry.getKey(), candidate)) {
					// this is a unit test class
					var testClass = this.easeModule.javaInstance.addTestClass(candidateEntry.getKey());
					if (candidate.hasOwnProperty("__description"))
						testClass.setDescription(candidate.__description);

					var testcases = new Array();
					var testClassSetup = null;
					var testClassTeardown = null;
					var testSetup = null;
					var testTeardown = null;

					for (test in candidate) {
						var annotations = this.getAnnotations(candidate[test]);

						if (annotations.hasOwnProperty("before"))
							testSetup = test;
						else if (annotations.hasOwnProperty("after"))
							testTeardown = test;
						else if (annotations.hasOwnProperty("beforeclass"))
							testClassSetup = test;
						else if (annotations.hasOwnProperty("afterclass"))
							testClassTeardown = test;
						else if ((annotations.hasOwnProperty("test")) || (test.match(/^test.*/) != null))
							testcases[testcases.length] = test;
					}

					if ((test.length > 0) && (testClassSetup != null))
						candidate[testClassSetup]();

					for (index in testcases) {
						var test = testcases[index];
						var annotations = this.getAnnotations(candidate[test]);

						this.easeModule.startTest(test, annotations["description"]);

						// register test start location
						try {
							// only works for Rhino debug engine
							var debugView = getScriptEngine().getContext().getDebuggableView(candidate[test]);
							file = this.easeModule.getTestFile().getResource()
							var script = new org.eclipse.ease.Script("", file, false);

							// line numbers are not sorted
							var debugFrame = new org.eclipse.ease.debugging.EaseDebugFrame(script, this
									.getFirstLineNumber(debugView.getLineNumbers()), -1);

							var stackTrace = new org.eclipse.ease.debugging.ScriptStackTrace();
							stackTrace.add(debugFrame);

							this.easeModule.getTest().setStackTrace(stackTrace);
						} catch (e) {
							// we could not set the stacktrace for the unit test
							// start location, ignore
						}

						if (candidate.hasOwnProperty("__ignore")) {
							this.easeModule.ignoreTest(candidate["__ignore"]);

						} else if (annotations.hasOwnProperty("ignore")) {
							this.easeModule.ignoreTest(annotations["ignore"]);

						} else {

							try {
								if (testSetup != null)
									candidate[testSetup]();

								try {
									this.easeModule.setTestTimeout(this.getTimeout(annotations));

									// execute the test
									candidate[test]();

									// check for expected exception
									var expectedException = this.getExpectedException(annotations);
									if (expectedException != null) {
										this.easeModule.javaInstance.failure("Expected exception not thrown: "
												+ expectedException, this.easeModule.getTest().getStackTrace());
									}

								} catch (e) {
									if (this.isAssertion(e)) {
										// test failure
										try {
											this.easeModule.javaInstance.failure(e.javaException.getMessage(),
													e.javaException.getScriptStackTrace());
										} catch (e1) {
											// no exception stacktrace available
											this.easeModule.failure(e.javaException.getMessage());
										}

									} else if (this.isExpectedException(annotations, e)) {
										// nothing to do, test is pass
									} else {
										// test error
										var message = e;
										if (typeof (e.javaException) !== 'undefined') {
											if (e.javaException.getMessage() != null)
												message = e.javaException.getMessage();
											else
												message = e.javaException.getClass().getSimpleName() + " thrown";
										}
												
										try {
											this.easeModule.javaInstance.error(message, e.javaException.getScriptStackTrace());
										} catch (e1) {
											// no exception stacktrace available
											this.easeModule.javaInstance.error(message, null);
										}
										
										// print exception to console
										if (typeof (e.javaException) !== 'undefined')
											e.javaException.printStackTrace(getScriptEngine().getErrorStream());
									}
								} finally {
									try {
										if (testTeardown != null)
											candidate[testTeardown]();
									} catch (e) {
										// test setup error
										var message = (typeof (e.javaException) !== 'undefined') ? e.javaException
												.getMessage() : e;
										try {
											this.easeModule.javaInstance.error("Test teardown error: " + message,
													e.getScriptStackTrace());
										} catch (e1) {
											// no exception stacktrace available
											this.easeModule.error("Test teardown error: " + message);
										}
									}
								}

							} catch (e) {
								// test setup error
								var message = (typeof (e.javaException) !== 'undefined') ? e.javaException.getMessage() : e;
								try {
									this.easeModule.javaInstance.error("Test setup error: " + message, e.getScriptStackTrace());
								} catch (e1) {
									// no exception stacktrace available
									this.easeModule.error("Test setup error: " + message);
								}
							}
						}

						this.easeModule.endTest();
					}

					if ((test.length > 0) && (testClassTeardown != null))
						candidate[testClassTeardown]();

					this.easeModule.javaInstance.addTestClass(null);
				}
			}
		},

		/**
		 * Get the lowest number in an unsorted array of line numbers
		 * 
		 * @param {array}
		 *            lineNumbers - unsorted line numbers of a function
		 * @return lowest line number
		 */
		getFirstLineNumber : function(lineNumbers) {
			var min = lineNumbers[0];
			for (index in lineNumbers) {
				if (lineNumbers[index] < min)
					min = lineNumbers[index];
			}

			return min;
		},

		/**
		 * Verify that an object is a unit test.
		 * 
		 * @param {object}
		 *            candidate - object to test
		 */
		isUnitTest : function(name, candidate) {
			if (name != '_') {
				try {
					return candidate.hasOwnProperty("__unittest");
				} catch (e) {
					return false;
				}
			}
		},

		/**
		 * Get annotations from a method. Annotations are simple string literals
		 * starting with an '@' at the beginning of the function code.
		 * 
		 * @param {function}
		 *            method - function to get annotations from
		 */
		getAnnotations : function(method) {
			var annotations = {};
			var data = method.toString();

			var expression = /@(\w+)(?:\((.*)\)["'])?;?/g;
			var match;

			do {
				match = expression.exec(data);
				if (match) {
					annotationContent = match[2];
					if (typeof(annotationContent) != 'undefined')
						annotationContent = annotationContent.replace(/\\\"/g, "\"");
						
					annotations[match[1].toLowerCase()] = annotationContent
				}
			} while (match);

			return annotations;
		},

		/**
		 * Check if a thrown exception was expected by the provided test function.
		 * 
		 * @param {array}
		 *            annotations - function annotations
		 * @param {exception}
		 *            e - thrown exception
		 */
		isExpectedException : function(annotations, e) {
			try {
				if (this.isJavaException(e))
					return (e.javaException.getClass().getName() == this.getExpectedException(annotations));

				else if (e instanceof java.lang.Throwable)
					return (e.getClass().getName() == this.getExpectedException(annotations));

			} catch (e1) {
			}

			return false;
		},

		/**
		 * Extract expected exception type from given method annotations.
		 * 
		 * @param {array}
		 *            annotations - method annotations
		 * @return expected java exception class name or <code>null</code>
		 */
		getExpectedException : function(annotations) {
			if (annotations.hasOwnProperty("expect"))
				return annotations["expect"];

			return null;
		},

		/**
		 * Validate if an exception is actually a wrapped java exception.
		 * 
		 * @param {Exception}
		 *            e - exception to query
		 * @return <code>true</code> when exception is a wrapped java exception
		 */
		isJavaException : function(e) {
			try {
				return (typeof (e.javaException) !== 'undefined');
			} catch (e1) {
			}

			return false;
		},

		/**
		 * Validate if an exception is actually a test assertion.
		 * 
		 * @param {Exception}
		 *            e - exception to query
		 * @return <code>true</code> when exception is an assertion
		 */
		isAssertion : function(e) {
			return this.isJavaException(e)
					&& e.javaException.getClass().equals(org.eclipse.ease.lang.unittest.AssertionException);
		},

		/**
		 * Get test timeout in [ms].
		 * 
		 * @param {array}
		 *            annotations - method annotations
		 * @return timeout in milliseconds or 0
		 */
		getTimeout : function(annotations) {
			if (annotations.hasOwnProperty("timeout"))
				return parseInt(annotations["timeout"]);

			return 0;
		},
	}

	// execute test runner
	__EASE_UnitTest_TestRunner.run();