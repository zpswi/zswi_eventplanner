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
    pk: number,
}

export const CalendarInitializer = () => {

    const init = () => {
        const calendarElement = document.getElementById('calendar')

        if (calendarElement === null) {
            return
        }

        const events = JSON.parse(calendarElement.dataset.events ?? '[]') as EventModel[]
        const mappedEvents = mapEvents(
            events.map(event => {
                return {
                    pk: event.pk,
                    event: event.fields
                }
            })
        )

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
            eventClick: (info) => {
                window.location.href = info.event.extendedProps.link
            }
        })

        calendar.render()
    }

    const mapEvents = (events: { pk: number, event: Event }[]) => {
        return events.map(entry => {
            return {
                title: entry.event.title,
                start: new Date(entry.event.start_time),
                end: new Date(entry.event.end_time),
                allDay: entry.event.all_day,
                link: `/app/event/${entry.pk}`
            }
        })
    }

    return {
        init
    }
}