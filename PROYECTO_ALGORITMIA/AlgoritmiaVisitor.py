# Generated from Algoritmia.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .AlgoritmiaParser import AlgoritmiaParser
else:
    from AlgoritmiaParser import AlgoritmiaParser

# This class defines a complete generic visitor for a parse tree produced by AlgoritmiaParser.

class AlgoritmiaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by AlgoritmiaParser#root.
    def visitRoot(self, ctx:AlgoritmiaParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#inss.
    def visitInss(self, ctx:AlgoritmiaParser.InssContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#ins.
    def visitIns(self, ctx:AlgoritmiaParser.InsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#input_.
    def visitInput_(self, ctx:AlgoritmiaParser.Input_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#output_.
    def visitOutput_(self, ctx:AlgoritmiaParser.Output_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#condition.
    def visitCondition(self, ctx:AlgoritmiaParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#while_.
    def visitWhile_(self, ctx:AlgoritmiaParser.While_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#reprod.
    def visitReprod(self, ctx:AlgoritmiaParser.ReprodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#agregado.
    def visitAgregado(self, ctx:AlgoritmiaParser.AgregadoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#corte.
    def visitCorte(self, ctx:AlgoritmiaParser.CorteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#procDef.
    def visitProcDef(self, ctx:AlgoritmiaParser.ProcDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#proc.
    def visitProc(self, ctx:AlgoritmiaParser.ProcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#assign.
    def visitAssign(self, ctx:AlgoritmiaParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#paramsId.
    def visitParamsId(self, ctx:AlgoritmiaParser.ParamsIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#paramsExpr.
    def visitParamsExpr(self, ctx:AlgoritmiaParser.ParamsExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#lista.
    def visitLista(self, ctx:AlgoritmiaParser.ListaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#consult.
    def visitConsult(self, ctx:AlgoritmiaParser.ConsultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#Mod.
    def visitMod(self, ctx:AlgoritmiaParser.ModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#Mul.
    def visitMul(self, ctx:AlgoritmiaParser.MulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#Var.
    def visitVar(self, ctx:AlgoritmiaParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#Parens.
    def visitParens(self, ctx:AlgoritmiaParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#Num.
    def visitNum(self, ctx:AlgoritmiaParser.NumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#sz.
    def visitSz(self, ctx:AlgoritmiaParser.SzContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#Lt.
    def visitLt(self, ctx:AlgoritmiaParser.LtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#Sum.
    def visitSum(self, ctx:AlgoritmiaParser.SumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#String.
    def visitString(self, ctx:AlgoritmiaParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#Nota.
    def visitNota(self, ctx:AlgoritmiaParser.NotaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#lst.
    def visitLst(self, ctx:AlgoritmiaParser.LstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#Eq.
    def visitEq(self, ctx:AlgoritmiaParser.EqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#Gt.
    def visitGt(self, ctx:AlgoritmiaParser.GtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#Div.
    def visitDiv(self, ctx:AlgoritmiaParser.DivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#Min.
    def visitMin(self, ctx:AlgoritmiaParser.MinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#consul.
    def visitConsul(self, ctx:AlgoritmiaParser.ConsulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#Get.
    def visitGet(self, ctx:AlgoritmiaParser.GetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#Let.
    def visitLet(self, ctx:AlgoritmiaParser.LetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#Neq.
    def visitNeq(self, ctx:AlgoritmiaParser.NeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#siz.
    def visitSiz(self, ctx:AlgoritmiaParser.SizContext):
        return self.visitChildren(ctx)



del AlgoritmiaParser