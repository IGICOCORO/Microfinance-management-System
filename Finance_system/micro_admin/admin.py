from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(LoanRepaymentEvery)
admin.site.register(Branch)
# admin.site.register(UserManager)
admin.site.register(Client)
admin.site.register(ClientBranchTransfer)
admin.site.register(Group)
admin.site.register(Centers)
admin.site.register(GroupMeetings)
admin.site.register(SavingsAccount)
admin.site.register(LoanAccount)
admin.site.register(GroupMemberLoanAccount)
admin.site.register(FixedDeposits)
admin.site.register(RecurringDeposits)
admin.site.register(Receipts)
admin.site.register(Payments)
