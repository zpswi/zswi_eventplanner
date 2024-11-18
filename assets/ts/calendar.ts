import {Calendar} from '@fullcalendar/core'
import interactionPlugin from '@fullcalendar/interaction'
import dayGridPlugin from '@fullcalendar/daygrid'
import timeGridPlugin from '@fullcalendar/timegrid'

type Event = {
    all_day: boolean,
    capacity: number,
    created_at: string,
    updated_at: string,
    description: string,
    start_time: string,
    end_time: string,
    location: string,
    title: string,
}

type EventModel = {
    fields: Event,
}

export const CalendarInitializer = () => {

    const init = () => {
        const calendarElement = document.getElementById('calendar')

        if (calendarElement === null) {
            return
        }

        const events = JSON.parse(calendarElement.dataset.events ?? '[]') as EventModel[]
        const mappedEvents = mapEvents(events.map(event => event.fields))

        const calendar = new Calendar(calendarElement, {
            plugins: [
                interactionPlugin,
                dayGridPlugin,
                timeGridPlugin,
            ],
            headerToolbar: {
                left: 'prev,next today',
                center: 'title',
                right: 'dayGridMonth,timeGridWeek,timeGridDay' // View switching buttons
            },
            themeSystem: 'bootstrap5',
            initialView: 'dayGridMonth',
            editable: true,
            events: mappedEvents,
        })

        calendar.render()
    }

    const mapEvents = (events: Event[]) => {
        return events.map(event => {
            return {
                title: event.title,
                start: new Date(event.start_time),
                end: new Date(event.end_time),
                allDay: event.all_day,
            }
        })
    }

    return {
        init
    }
}