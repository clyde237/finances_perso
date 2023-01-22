from flask import render_template, redirect, url_for, flash, request
from app import app
from .forms import ExpenseForm, IncomeForm
from .models import Expense, Income
from app import db
from datetime import datetime

@app.route('/')
def index():
    expenses = Expense.query.filter_by(user_id=current_user.id).all()
    incomes = Income.query.filter_by(user_id=current_user.id).all()
    return render_template('index.html', expenses=expenses, incomes=incomes)

@app.route('/add_expense', methods=['GET', 'POST'])
@login_required
def add_expense():
    form = AddExpenseForm()
    if form.validate_on_submit():
        expense = Expense(name=form.name.data, amount=form.amount.data, category=form.category.data, date=form.date.data, user_id=current_user.id)
        db.session.add(expense)
        db.session.commit()
        flash('Expense added successfully')
        return redirect(url_for('index'))
    return render_template('add_expense.html', form=form)

@app.route('/add_income', methods=['GET', 'POST'])
@login_required
def add_income():
    form = AddIncomeForm()
    if form.validate_on_submit():
        income = Income(name=form.name.data, amount=form.amount.data, category=form.category.data, date=form.date.data, user_id=current_user.id)
        db.session.add(income)
        db.session.commit()
        flash('Income added successfully')
        return redirect(url_for('index'))
    return render_template('add_income.html', form=form)

@app.route('/edit_expense/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_expense(id):
    expense = Expense.query.get(id)
    if expense.user_id != current_user.id:
        flash("You don't have permission to edit this expense")
        return redirect(url_for('index'))
    form = EditExpenseForm(obj=expense)
    if form.validate_on_submit():
        form.populate_obj(expense)
        db.session.commit()
        flash('Expense edited successfully')
        return redirect(url_for('index'))
    return render_template('edit_expense.html', expense=expense, form=form)

@app.route('/edit_income/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_income(id):
    income = Income.query.get(id)
    if income.user_id != current_user.id:
        flash("You don't have permission to edit this income")
        return redirect(url_for('index'))
    form = EditIncomeForm(obj=income)
    if form.validate_on_submit():
        form.populate_obj(income)
        db.session.commit()
        flash('Income edited successfully')
        return redirect(url_for('index'))
    return render_template('edit_income.html', income=income, form=form)

@app.route('/delete_expense/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_expense(id):
    expense = Expense.query.get(id)
    if expense.user_id != current_user.id:
        flash("You don't have permission to delete this expense")
        return redirect(url_for('index'))
    form = ConfirmDeletionForm()
    if form.validate_on_submit():
        db.session.delete(expense)
        db.session.commit()
        flash('Expense deleted successfully')
        return redirect(url_for('index'))
    return render_template('delete_expense.html', expense=expense, form=form)


@app.route('/delete_income/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_income(id):
    income = Income.query.get(id)
    if income.user_id != current_user.id:
        flash("You don't have permission to delete this income")
        return redirect(url_for('index'))
    form = ConfirmDeletionForm()
    if form.validate_on_submit():
        db.session.delete(income)
        db.session.commit()
        flash('Income deleted successfully')
        return redirect(url_for('index'))
    return render_template('delete_income.html', income=income, form=form)


