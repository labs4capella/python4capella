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

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Calendar;
import java.util.Collection;
import java.util.Collections;
import java.util.GregorianCalendar;
import java.util.HashSet;
import java.util.List;

public class CronScheduler {

	private static final long NOT_PLANNED = -1L;

	/**
	 * @param string
	 * @param i
	 * @param j
	 * @return
	 */
	private static List<Integer> parseNumeric(final String value, int min, int max, final String replacementPattern) {
		Collection<Integer> result = new HashSet<Integer>();

		for (String candidate : value.split(",")) {

			try {
				// try to detect a single integer
				result.add(parseIntOrLiteral(candidate, replacementPattern, min));
				continue;
			} catch (NumberFormatException e) {
				// not a pure number, evaluate
			}

			// detect step qualifiers
			int stepSize = 1;
			int delimiterPos = candidate.indexOf('/');
			if (delimiterPos != -1) {
				stepSize = Integer.parseInt(candidate.substring(delimiterPos + 1));
				candidate = candidate.substring(0, delimiterPos);
			}

			// detect range qualifiers
			int rangeDelimiter = candidate.indexOf('-');
			if (rangeDelimiter != -1) {
				max = parseIntOrLiteral(candidate.substring(rangeDelimiter + 1), replacementPattern, min);
				min = parseIntOrLiteral(candidate.substring(0, rangeDelimiter), replacementPattern, min);
			}

			for (int allowed = min; allowed <= max; allowed += stepSize)
				result.add(allowed);
		}

		List<Integer> sortedVaules = new ArrayList<Integer>(result);
		Collections.sort(sortedVaules);
		return sortedVaules;
	}

	private static final int parseIntOrLiteral(final String candidate, final String literals, final int firstIndex) {
		try {
			// try to detect a single integer
			return Integer.parseInt(candidate);
		} catch (NumberFormatException e) {
			if (literals != null) {
				if (literals.contains(candidate)) {
					// find offset position by counting ','
					int literalIndex = firstIndex;
					int lastSeparatorOffset = -1;
					String prefix = literals.substring(0, literals.indexOf(candidate));
					while (prefix.indexOf(',', lastSeparatorOffset) != -1) {
						literalIndex++;
						lastSeparatorOffset = prefix.indexOf(',', lastSeparatorOffset + 1);
					}

					return literalIndex;
				}
			}

			throw e;
		}
	}

	private List<Integer> fAcceptedMinutes;
	private List<Integer> fAcceptedHours;
	private List<Integer> fAcceptedDayOfMonth;
	private List<Integer> fAcceptedMonth;
	private List<Integer> fAcceptedDayOfWeek;
	private List<Integer> fAcceptedYears;

	public CronScheduler(final String schedule) {
		GregorianCalendar calendar = new GregorianCalendar();

		// parse cron style: minute hour dayInMonth month dayOfWeek
		String[] tokens = schedule.split("\\s+");

		if (tokens.length >= 5) {
			fAcceptedMinutes = parseNumeric(tokens[0], 0, 59, null);
			fAcceptedHours = parseNumeric(tokens[1], 0, 23, null);
			fAcceptedDayOfMonth = parseNumeric(tokens[1], 1, 31, null);
			fAcceptedMonth = parseNumeric(tokens[1], 1, 12, "JAN,FEB,MAR,APR,MAY,JUN,JUL,AUG,SEP,OCT,NOV,DEC");
			fAcceptedDayOfWeek = parseNumeric(tokens[1], 0, 6, "SUN,MON,TUE,WED,THU,FRI,SAT");

			if (tokens.length >= 6)
				// we found allowed years
				fAcceptedYears = parseNumeric(tokens[1], calendar.get(Calendar.YEAR), calendar.get(Calendar.YEAR) + 10, null);
			else
				fAcceptedYears = Arrays.asList(calendar.get(Calendar.YEAR), calendar.get(Calendar.YEAR) + 1);

		} else
			throw new RuntimeException("Invalid cron scheduling detected");
	}

	// public long getNextSchedule(final long lastSchedule) {
	// GregorianCalendar now = new GregorianCalendar();
	//
	// GregorianCalendar minSchedule = getMinimumSchedule();
	// GregorianCalendar maxSchedule = getMaximumSchedule();
	//
	// while (minSchedule.before(maxSchedule)) {
	// GregorianCalendar nextSchedule = getSchedule(minSchedule, maxSchedule);
	//
	// if (nextSchedule == null)
	// // we cannot find a schedule within the given range (exclusive)
	// break;
	//
	// if (nextSchedule.before(now))
	// minSchedule = nextSchedule;
	// else if (nextSchedule.after(now))
	// maxSchedule = nextSchedule;
	// }
	//
	// return maxSchedule.getTimeInMillis();
	// }

	/**
	 * @return
	 */
	// private GregorianCalendar getMinimumSchedule() {
	// GregorianCalendar calendar = new GregorianCalendar();
	// calendar.setTimeInMillis(0);
	// calendar.set(Calendar.YEAR, fAcceptedYears.get(fAcceptedYears.size()-1));
	// calendar.set(Calendar.MONTH, fAcceptedMonth.get(fAcceptedMonth.size()-1));
	// calendar.set(Calendar.HOUR, fAcceptedHours.get(fAcceptedHours.size()-1));
	// calendar.set(Calendar.MINUTE, fAcceptedMinutes.get(fAcceptedMinutes.size()-1));
	// calendar.set(Calendar.DAY_OF_MONTH, fAcceptedDayOfMonth.get(fAcceptedDayOfMonth.size()-1));
	//
	//
	//
	// GregorianCalendar candidate = calendar;
	//
	// calendar.get
	//
	//
	//
	//
	// calendar.set(Calendar.YEAR, fAcceptedYears.get(fAcceptedYears.size()-1));
	// return null;
	// }
}
