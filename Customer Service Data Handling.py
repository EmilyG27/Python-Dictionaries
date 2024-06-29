def open_ticket(ticket, id, customer, issue, status):
    if id not in ticket:
        ticket[id] = {"Customer": customer, "Issue": issue, "Status": status}
        print(f"{ticket}{id} added.")

def update_ticket(ticket, id, status):
    if id in ticket:
        ticket[id]["Status"] = status
        print(f"{id} has been updated")
    else:
        print(f"{id} not found.")

def display_tickets(ticket):
    for id, (customer, issue, status) in ticket.items():
        print(f"{ticket}{id}:, {customer}, {issue}, {status} ")
        break


service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

open_ticket(service_tickets, "Ticket003", "Mary", "Tracking issue", "open")
update_ticket(service_tickets, "Ticket001", "closed")
display_tickets(service_tickets)