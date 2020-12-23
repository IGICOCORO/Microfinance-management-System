from django.urls import path
from .views import *

urlpatterns = [

    path('', index, name='microadmin_index'),
    path('login/', getin, name='login'),
    path('logout/', getout, name="logout"),
    # ------------------------------------------- #
    # Branch model paths
    path('branch/create/', create_branch_view, name='createbranch'),
    path('branch/edit/(<pk>)/', update_branch_view, name='editbranch'),
    path('branch/view/', branch_list_view, name='viewbranch'),
    path('branch/delete/(<pk>)/',
         branch_inactive_view, name='deletebranch'),
    path('branch/profile/(<pk>)/',
         branch_profile_view, name='branchprofile'),
    # ------------------------------------------- #
    # User model paths
    path('users/list/', users_list_view, name='userslist'),
    path('user/create/', create_user_view, name='createuser'),
    path('user/edit/(<pk>)/', update_user_view, name='edituser'),
    path('user/profile/(<pk>)/', user_profile_view, name='userprofile'),
    path('user/delete/(<pk>)/', user_inactive_view, name='deleteuser'),
    # ------------------------------------------- #
    # Client model paths
    path('clients/list/', clients_list_view, name='viewclient'),
    path('client/create/', create_client_view, name='createclient'),
    path('client/edit/(<pk>)/', update_client_view, name='editclient'),
    path('client/delete/(<pk>)/',
         client_inactive_view, name='deleteclient'),
    path('client/profile/(<pk>)/',
         client_profile_view, name='clientprofile'),
    path('client/profile/update/(<pk>+)/',
         updateclientprofileview, name='updateclientprofile'),
    # ------------------------------------------- #
    # Group
    path('group/create/', create_group_view, name='creategroup'),
    path('group/(<group_id>)/profile/',
         group_profile_view, name='groupprofile'),
    path('groups/list/', groups_list_view, name='groupslist'),
    path('group/(<group_id>)/delete/',
         group_inactive_view, name='deletegroup'),

    # Group - Assign Staff
    path('group/(<group_id>)/assign-staff/',
         group_assign_staff_view, name='assignstaff'),

    # Group Members (add, remove, view)
    path('group/(<group_id>)/members/add/',
         group_add_members_view, name='addmember'),
    path('group/(<group_id>)/members/list/',
         group_members_list_view, name='viewmembers'),
    path('group/(<group_id>)/member/(<client_id>)/remove/',
         group_remove_members_view, name='removemember'),

    # Group Meeting (list, add)
    path('group/(<group_id>)/meetings/list/',
         group_meetings_list_view, name='groupmeetings'),
    path('group/(<group_id>)/meetings/add/',
         group_meetings_add_view, name='addgroupmeeting'),

    # Receipts(create, list)
    path('transactions/', transactions, name="transactions"),
    path('deposits/', deposits, name="deposits"),
    path('reports/', reports, name="reports"),
    # path('^receiptsdeposit/', receipts_deposit, name="receiptsdeposit"),
    path('receiptslist/', receipts_list, name="receiptslist"),

    path('generalledger/', general_ledger, name="generalledger"),
    path('fixeddeposits/', fixed_deposits_view, name="fixeddeposits"),
    path('clientfixeddepositsprofile/(<fixed_deposit_id>)/',
         client_fixed_deposits_profile, name="clientfixeddepositsprofile"),
    path('viewclientfixeddeposits/', view_client_fixed_deposits,
         name="viewclientfixeddeposits"),

    # Day Book
    path('viewdaybook/', day_book_view, name="viewdaybook"),
    path('viewparticularclientfixeddeposits/(<client_id>)/',
         view_particular_client_fixed_deposits, name="viewparticularclientfixeddeposits"),
    # path('^payslip/', pay_slip, name="payslip"),
    path('paymentslist/', payments_list, name="paymentslist"),
    path('recurringdeposits/', recurring_deposits_view,
         name="recurringdeposits"),
    path('clientrecurringdepositsprofile/(<recurring_deposit_id>)/',
         client_recurring_deposits_profile, name="clientrecurringdepositsprofile"),
    path('viewclientrecurringdeposits/', view_client_recurring_deposits,
         name="viewclientrecurringdeposits"),
    path('viewparticularclientrecurringdeposits/(<client_id>)/',
         view_particular_client_recurring_deposits, name="viewparticularclientrecurringdeposits"),
    # path('^generalledgerpdfdownload/', GeneralLedgerPdfDownload, name="generalledgerpdfdownload"),
    path('daybookpdfdownload/(<date>{4}-{2}-{2})/',
         daybook_pdf_download, name="daybookpdfdownload"),
    path('userchangepassword/', user_change_password, name="userchangepassword"),
]
