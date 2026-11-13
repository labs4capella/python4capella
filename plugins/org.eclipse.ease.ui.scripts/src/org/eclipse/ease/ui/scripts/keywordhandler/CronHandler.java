/*******************************************************************************
 * Copyright (c) 2016 Christian Pontesegger and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v2.0
 * which accompanies this distribution, and is available at
 * https://www.eclipse.org/legal/epl-2.0/
 *
 * SPDX-License_Identifier: EPL-2.0
 *
 * Contributors:
 *     Christian Pontesegger - initial API and implementation
 *******************************************************************************/

package org.eclipse.ease.ui.scripts.keywordhandler;

import java.util.Calendar;
import java.util.Collection;
import java.util.GregorianCalendar;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.eclipse.ease.ui.scripts.repository.IScript;
import org.osgi.service.event.Event;
import org.osgi.service.event.EventHandler;

public class CronHandler implements EventHandler {

	private final Map<IScript, Long> fScheduledScripts = new HashMap<IScript, Long>();

	private final Map<IScript, Long> fPastExecutions = new HashMap<IScript, Long>();

	@Override
	public void handleEvent(final Event event) {
		IScript script = (IScript) event.getProperty("script");
		String value = (String) event.getProperty("value");
		String oldValue = (String) event.getProperty("oldValue");

		if (!oldValue.isEmpty())
			// remove eventually planned execution
			fScheduledScripts.remove(script);

		planExecution(script, value);
	}

	// private long parseTime(final IScript script, final String scheduledTime) {
	// long lastExecution = (fPastExecutions.containsKey(script)) ? fPastExecutions.get(script) : 0;
	// GregorianCalendar calendar = new GregorianCalendar();
	//
	// if (scheduledTime.startsWith("@")) {
	// calendar.setTimeInMillis(lastExecution);
	//
	// switch (scheduledTime) {
	// case "@hourly":
	// calendar.add(Calendar.HOUR, 1);
	// calendar.set(Calendar.MINUTE, 0);
	// calendar.set(Calendar.SECOND, 0);
	// calendar.set(Calendar.MILLISECOND, 0);
	// break;
	//
	// case "@daily":
	// break;
	//
	// case "@weekly":
	// calendar.add(Calendar.DAY_OF_MONTH, 7);
	//
	// calendar.set(Calendar.DAY_OF_WEEK, Calendar.MONDAY);
	// calendar.set(Calendar.AM_PM, 0);
	// calendar.set(Calendar.HOUR, 0);
	// calendar.set(Calendar.MINUTE, 0);
	// calendar.set(Calendar.SECOND, 0);
	// calendar.set(Calendar.MILLISECOND, 0);
	//
	// break;
	//
	// case "@monthly":
	// calendar.add(Calendar.MONTH, 1);
	//
	// calendar.set(Calendar.DAY_OF_MONTH, 1);
	// calendar.set(Calendar.AM_PM, 0);
	// calendar.set(Calendar.HOUR, 0);
	// calendar.set(Calendar.MINUTE, 0);
	// calendar.set(Calendar.SECOND, 0);
	// calendar.set(Calendar.MILLISECOND, 0);
	// break;
	//
	// case "@annually":
	// // fall through
	// case "@yearly":
	// calendar.add(Calendar.YEAR, 1);
	//
	// calendar.set(Calendar.MONTH, 1);
	// calendar.set(Calendar.DAY_OF_MONTH, 1);
	// calendar.set(Calendar.AM_PM, 0);
	// calendar.set(Calendar.HOUR, 0);
	// calendar.set(Calendar.MINUTE, 0);
	// calendar.set(Calendar.SECOND, 0);
	// calendar.set(Calendar.MILLISECOND, 0);
	// break;
	//
	// default:
	// Logger.error(Activator.PLUGIN_ID, "Invalid cron scheduling detected in script: " + script.getLocation());
	// return NOT_PLANNED;
	// }
	//
	// return calendar.getTimeInMillis();
	//
	// } else {
	// // parse cron style: minute hour dayInMonth month dayOfWeek
	// String[] tokens = scheduledTime.split("\\s+");
	//
	// if (tokens.length >= 5) {
	// // 5 tokens are mandatory
	// List<Integer> acceptedMinutes = parseNumeric(tokens[0], 0, 59, null);
	// List<Integer> acceptedHours = parseNumeric(tokens[1], 0, 23, null);
	// List<Integer> acceptedDayOfMonth = parseNumeric(tokens[1], 1, 31, null);
	// List<Integer> acceptedMonth = parseNumeric(tokens[1], 1, 12, "JAN,FEB,MAR,APR,MAY,JUN,JUL,AUG,SEP,OCT,NOV,DEC");
	// List<Integer> acceptedDayOfWeek = parseNumeric(tokens[1], 0, 6, "SUN,MON,TUE,WED,THU,FRI,SAT");
	//
	// List<Integer> acceptedYears;
	// if (tokens.length >= 6)
	// // we found allowed years
	// acceptedYears = parseNumeric(tokens[1], calendar.get(Calendar.YEAR), calendar.get(Calendar.YEAR) + 10, null);
	// else
	// acceptedYears = Arrays.asList(calendar.get(Calendar.YEAR), calendar.get(Calendar.YEAR) + 1);
	//
	// findNextDate(lastExecution, acceptedMinutes, acceptedHours, acceptedDayOfMonth, acceptedMonth, acceptedDayOfWeek, acceptedYears);
	//
	// calendar.set(Calendar.MINUTE, acceptedMinutes.get(0));
	// calendar.set(Calendar.HOUR, acceptedHours.get(0));
	// calendar.set(Calendar.DAY_OF_MONTH, acceptedDayOfMonth.get(0));
	// calendar.set(Calendar.MONTH, acceptedMonth.get(0));
	//
	// } else {
	// Logger.error(Activator.PLUGIN_ID, "Invalid cron scheduling detected in script: " + script.getLocation());
	// return NOT_PLANNED;
	// }
	// }
	// }

	/**
	 * @param lastExecution
	 * @param acceptedMinutes
	 * @param acceptedHours
	 * @param acceptedDayOfMonth
	 * @param acceptedMonth
	 * @param acceptedDayOfWeek
	 * @param acceptedYears
	 */
	private static void findNextDate(final long lastExecution, final List<Integer> acceptedMinutes, final List<Integer> acceptedHours,
			final List<Integer> acceptedDayOfMonth, final List<Integer> acceptedMonth, final List<Integer> acceptedDayOfWeek,
			final List<Integer> acceptedYears) {

		GregorianCalendar lastTime = new GregorianCalendar();
		lastTime.setTimeInMillis(lastExecution);

		GregorianCalendar now = new GregorianCalendar();

		GregorianCalendar nextTime = new GregorianCalendar();
		nextTime.setTimeInMillis(now.getTimeInMillis());

		nextTime.set(Calendar.YEAR, acceptedYears.get(0));
		nextTime.set(Calendar.MONTH, acceptedMonth.get(0));
		nextTime.set(Calendar.HOUR, acceptedHours.get(0));
		nextTime.set(Calendar.MINUTE, acceptedMinutes.get(0));
		nextTime.set(Calendar.DAY_OF_MONTH, acceptedDayOfMonth.get(0));

		GregorianCalendar tempDate = new GregorianCalendar();
		while (nextTime.before(now)) {
			tempDate.setTimeInMillis(nextTime.getTimeInMillis());

			// if ()

		}

	}

	/**
	 * @param acceptedMinutes
	 * @param i
	 * @return
	 */
	private static int findNext(final Collection<Integer> acceptedValues, final int current) {

		int minimum = 10000;
		int next = 10000;
		for (int candidate : acceptedValues) {
			minimum = Math.min(candidate, minimum);
			if ((candidate >= current) && (candidate < next))
				next = candidate;
		}

		return (next != 10000) ? next : minimum;
	}

	/**
	 * @param script
	 * @param value
	 */
	private void planExecution(final IScript script, final String scheduledTime) {

	}
}
